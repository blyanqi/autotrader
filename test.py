import pyautogui

# 获取屏幕尺寸
# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)

# 获取鼠标当前位置
# x, y = pyautogui.position()
# print(x, y)
# 判断坐标是否在屏幕内
# res = pyautogui.onScreen(x, y)
# print(res)

# 鼠标移动到指定位置
# pyautogui.moveTo(550, 100)
# 鼠标移动到指定位置,耗时0.5
# pyautogui.moveTo(1000, 150, duration=0.5)
# pyautogui.moveTo(1000, 150, duration=2, tween=pyautogui.easeInOutQuad)
# pyautogui.easeInQuad 开始很慢，不断加速
# pyautogui.easeOutQuad 开始快，然后减速
# pyautogui.easeInOutQuad 开始和结束都快，中间比较慢
# pyautogui.easeInBounce 一步一徘徊前进
# pyautogui.easeInElastic 徘徊幅度更大，甚至超过起点和终点

# 鼠标拖动到指定位置
# pyautogui.dragTo(1150, 300, button='left')
# 耗时 2 秒
# pyautogui.dragTo(1150, 300, 2, button='right')

# 鼠标点击
pyautogui.click()
# 移动到指定位置后点击，耗时 1 秒
pyautogui.click(100, 200, duration=1)
# 通过button参数设置left，middle和right三个键
pyautogui.click(button='right', clicks=2, interval=0.25)
# 两次点击，间隔 0.24秒
pyautogui.click(clicks=2, interval=0.25)
# 点击
pyautogui.rightClick(100, 100)
pyautogui.middleClick(100, 100)
pyautogui.doubleClick(100, 100)
pyautogui.tripleClick(100, 100)

pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
