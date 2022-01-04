import pyautogui
import time
import win32gui
import easyocr
import numpy
import re

from abc import ABCMeta, abstractmethod

# 开启失败保护
pyautogui.FAILSAFE = True
# init OCR
reader = easyocr.Reader(['ch_sim'], gpu=True)


class ClickWork(metaclass=ABCMeta):

    @abstractmethod
    def get_point(get_point_info) -> pyautogui.Point:
        ...

    def click(self, get_point_info, effective_count=1, x_offset=0, y_offset=0, pause=2,
              stop_point=None, stop_point_info=None):

        # 执行到满足终止条件时
        if effective_count <= -1:
            while stop_point is None or stop_point.get_point(stop_point_info) is None:
                point = self.get_point(get_point_info)
                if point is not None:
                    pyautogui.click(point.x + x_offset, point.y + y_offset)
                else:
                    print(
                        f"未找到{get_point_info}, 需要点击{effective_count}, {pause}秒后重试")
                time.sleep(pause)

        # 执行一次 不管成功还是失败
        elif effective_count == 0:
            point = self.get_point(get_point_info)
            if point is not None:
                pyautogui.click(point.x + x_offset, point.y + y_offset)
            else:
                print(
                    f"未找到{get_point_info}, 需要点击{effective_count}")

        # 执行有效次数 只计算成功次数
        else:
            current_effective_count = 0
            while effective_count > current_effective_count:
                point = self.get_point(get_point_info)
                if point is not None:
                    pyautogui.click(point.x + x_offset, point.y + y_offset)
                    current_effective_count = current_effective_count + 1
                else:
                    print(
                        f"未找到{get_point_info}, 需要点击{effective_count}, 已点击{current_effective_count}, {pause}秒后重试")
                time.sleep(pause)

        print(f"执行完毕:{get_point_info}")


class ImgClick(ClickWork):
    def get_point(self, get_point_info) -> pyautogui.Point:
        return pyautogui.locateCenterOnScreen(get_point_info)


class WindowClick(ClickWork):

    def get_point(self, get_point_info) -> pyautogui.Point:

        window = win32gui.FindWindow(None, get_point_info)
        if window is None:
            return None

        rect = win32gui.GetWindowRect(window)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        return pyautogui.Point(w / 2 + x, (h / 5) * 4 + y)


class TextClick(ClickWork):

    def get_point(self, get_point_info) -> pyautogui.Point:

        screenshot = pyautogui.screenshot()
        img_byte = numpy.asarray(screenshot)

        ocr_result = reader.readtext(img_byte)

        for res in ocr_result:
            print(res)
            if get_point_info == res[1]:
                coordinate = res[0]
                x = coordinate[0][0]
                y = coordinate[0][1]
                w = coordinate[1][0] - x
                h = coordinate[3][1] - y
                return pyautogui.Point(w / 2 + x, h / 2 + y)

        return None

    def search(self, pattern: str) -> str:

        screenshot = pyautogui.screenshot()
        img_byte = numpy.asarray(screenshot)

        ocr_result = reader.readtext(img_byte)

        for res in ocr_result:
            print(res)
            if re.search(pattern, res[1], re.M) is not None:
                return res[1]

        return None
