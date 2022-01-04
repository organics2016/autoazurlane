# AutoAzurLane

AutoAzurLane 是碧蓝航线的自动化脚本，但不仅限于碧蓝航线或者其他游戏。理论上你只需要简单的修改即可适配很多日常点击操作。<br>

## Runtime

- Windows 10 and last
- Python 3.8.x - 3.9.x

## Dependencies
- [pyautogui](https://github.com/asweigart/pyautogui) - 用于获取截图和模拟鼠标点击等操作
- [pywin32](https://github.com/mhammond/pywin32) - 用于获取用户窗口坐标和截图等操作
- [easyocr](https://github.com/JaidedAI/EasyOCR) - OCR 识别
- [pytorch 1.10.1](https://pytorch.org/get-started/locally/) - easyocr 在 Windows 平台下工作的必须依赖
- [CUDA Toolkit 11.3.0](https://developer.nvidia.cn/cuda-toolkit-archive) - easyocr 使用GPU情况下必须依赖，并且版本一定要与pytorch的指定版本相同

## Installation
1. Clone this repository
```
git clone https://github.com/organics2016/autoazurlane.git
```

2. 如果你是N卡并且需要GPU支持，先下载安装 [CUDA Toolkit 11.3.0](https://developer.nvidia.cn/cuda-toolkit-archive) 然后再执行下面的命令安装 pytorch。这里是以 [pytorch 1.10.1](https://pytorch.org/get-started/locally/) 为例安装，具体情况需要参考 pytorch 指定的 CUDA 版本
```
pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

```

如果你不需要GPU支持，则可以直接安装 pytorch
```
pip install torch torchvision torchaudio
```

根据不同的选择，你需要在项目的 click.py 文件进行配置是否启用GPU，默认情况下是启用的。
```python
reader = easyocr.Reader(['ch_sim'], gpu=True)
```


3. 安装剩余依赖

```
pip install pywin32
pip install pyautogui

```

## Usage

```
python autoazurlane.py
```

autoazurlane.py 文件实际上也是一个使用示例，实现了 碧蓝航线 演习 `exercise`、主线`main_battle`等日常

```python
# 文本点击
text_click = TextClick()
# 窗口点击
window_click = WindowClick()
# 图片点击
img_click = ImgClick()


def main():
    print("starting......")

    # 找到屏幕上 "出击" 文本位置并点击1次 如果没有则会阻塞(block) 直到点击1次为止
    text_click.click('出击')

    # 找到屏幕上 "出击" 文本位置 以文本中心位置为原点，下移200像素(文本中心位置为原点，X轴左负右正，Y轴上负下正) 并点击2次 如果没有则会阻塞(block) 直到点击2次为止
    text_click.click('出击', 2, 0, 200)

    # 找到屏幕上 "出击" 文本位置并一直点击，直到屏幕上出现 "确定"
    text_click.click('出击', -1, 0, 0, 2, text_click, '确定')

    # 找到屏幕上 a.png 截图位置并点击1次 如果没有则会阻塞(block) 直到点击1次为止
    img_click.click('img/a.png')

    # 找到名为 xxx 的窗口 在窗口正下方1/5处点击1次 如果没有则会阻塞(block) 直到点击1次为止
    window_click.click('xxx')


if __name__ == '__main__':
    main()

```



