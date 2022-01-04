from ctypes.wintypes import BOOL
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


def main_battle(battle_chapter: int, battle_name: str, highLevel: bool, count: int):

    click_text.click('出击')
    click_text.click('主线')

    chapter: str = click_text.search('^第\\d+章$')

    if chapter is None:
        raise Exception('无法定位当前主线章节')

    current_chapter = int(chapter[1:chapter.rfind('章')])
    while battle_chapter != current_chapter:

        if battle_chapter < current_chapter:
            click_text.click('上一章')
            current_chapter = current_chapter - 1
        else:
            click_text.click('下一章')
            current_chapter = current_chapter + 1

    if highLevel:
        if click_text.get_point('困难') is not None:
            click_text.click('困难')
    else:
        if click_text.get_point('普通') is not None:
            click_text.click('普通')

    click_text.click(battle_name)
    click_text.click('立刻前往', 2)

    again(count)


def again(count: int):

    for num in range(count):
        click_window.click('碧蓝航线 - MuMu模拟器', -1, 0, 0, 2, click_text, '再次前往')
        click_text.click('再次前往')


def main():
    print("starting......")

    # exercise(10)

    main_battle(7, '7-2短兵相接', True, 3)

    # again(200)


if __name__ == '__main__':
    main()
