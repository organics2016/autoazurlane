from click import TextClick, WindowClick, ImgClick

# 文本点击
text_click = TextClick()
# 窗口点击
window_click = WindowClick()
# 图片点击
img_click = ImgClick()

# 点击指定窗口 宽50% 高80%  无意义点击，用于战斗结束后的结算页面
w_click_info = type('', (), {'window_name': '碧蓝航线 - MuMu模拟器',
                             'w_coefficient': 0.5, 'h_coefficient': 0.8})()

# 返回按钮
w_click_esc = type('', (), {'window_name': '碧蓝航线 - MuMu模拟器',
                            'w_coefficient': 0.045, 'h_coefficient': 0.105})()


# 开始演习坐标
w_click_start_exercise = type('', (), {'window_name': '碧蓝航线 - MuMu模拟器',
                                       'w_coefficient': 0.5, 'h_coefficient': 0.75})()


def test():

    img_click.click('img/back.png', -1)


def exercise(count: int):

    text_click.click('出击')
    text_click.click('演习')

    for num in range(count):
        text_click.click('演习', 1, 0, 200)
        # text_click.click('开始演习')
        window_click.click(w_click_start_exercise)
        text_click.click('出击')
        window_click.click(w_click_info, -1, 0, 0, 2, text_click, '确定')
        text_click.click('确定')
        text_click.click('点击关闭', -1, 0, 0, 2, text_click, '演习')


def main_battle(battle_chapter: int, battle_name: str, highLevel: bool, count: int):

    text_click.click('出击')
    text_click.click('主线')

    chapter: str = text_click.search('^第\\d+章$')

    if chapter is None:
        raise Exception('无法定位当前主线章节')

    current_chapter = int(chapter[1:chapter.rfind('章')])
    while battle_chapter != current_chapter:

        if battle_chapter < current_chapter:
            text_click.click('上一章', 1, 0, -80)
            current_chapter = current_chapter - 1
        else:
            text_click.click('下一章', 1, 0, -80)
            current_chapter = current_chapter + 1

    if highLevel:
        if text_click.get_point('困难') is not None:
            text_click.click('困难')
    else:
        if text_click.get_point('普通') is not None:
            text_click.click('普通')

    text_click.click(battle_name)
    text_click.click('立刻前往', 2)

    again(count)


def again(count: int):

    for num in range(count):
        window_click.click(w_click_info, -1, 0, 0, 2, text_click, '再次前往')
        text_click.click('再次前往')


def main():
    print("starting......")

    # test()

    exercise(10)

    # window_click.click(w_click_esc, 2)
    img_click.click('img/back.png', 2)

    main_battle(7, '7-2短兵相接', True, 3)

    # again(200)


if __name__ == '__main__':
    main()
