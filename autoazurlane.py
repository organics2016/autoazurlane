from click import ClickText, ClickWindow

click_text = ClickText()
click_window = ClickWindow()


def test(info: str):

    # while True:
    #     again = pyautogui.locateCenterOnScreen(img)
    #     print(again)
    #     time.sleep(2)

    click_window.click('碧蓝航线 - MuMu模拟器', -1)


def exercise(count: int):

    click_text.click('出击')
    click_text.click('演习')

    for num in range(count):
        click_text.click('演习', 1, 0, 200)
        click_text.click('开始演习')
        click_text.click('出击')
        click_window.click('碧蓝航线 - MuMu模拟器', -1, 0, 0, 2, click_text, '确定')
        click_text.click('确定')
        click_text.click('点击关闭', -1, 0, 0, 2, click_text, '演习')


def difficulty(count: int):

    click_text.click('出击')
    click_text.click('主线')
    click_text.click('7-2短兵相接')
    click_text.click('立刻前往', 2)

    again(count)


def again(count: int):

    for num in range(count):
        click_window.click('碧蓝航线 - MuMu模拟器', -1, 0, 0, 2, click_text, '再次前往')
        click_text.click('再次前往')


def main():
    print("starting......")

    # exercise(10)
    # difficulty(3)

    again(2)


if __name__ == '__main__':
    main()
