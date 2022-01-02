from click import ClickText, ClickWindow


def test(info: str):

    # while True:
    #     again = pyautogui.locateCenterOnScreen(img)
    #     print(again)
    #     time.sleep(2)

    c = ClickText()
    while True:
        print(c.get_point(info))
    # ClickText().click('演习')


def exercise(count: int):

    for num in range(count):
        ClickText().click('演习', 1, 0, 200)
        ClickText().click('开始演习')
        ClickText().click('出击')
        ClickWindow().click('碧蓝航线 - MuMu模拟器', -1, 0, 0, 2, ClickText(), '确定')
        ClickText().click('确定')
        ClickText().click('点击关闭', -1, 0, 0, 2, ClickText(), '演习')


def main():
    print("starting......")
    exercise(10)


if __name__ == '__main__':
    main()
