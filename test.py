import win32gui


def callback(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))
    print(w/2+x, h/2+y)


def main():
    callback(win32gui.FindWindow(None, '碧蓝航线 - MuMu模拟器'))


if __name__ == '__main__':
    main()
