"""在终端中显示跑马灯（滚动）文字"""


import time
import os

s = "北京欢迎您"

while True:
    os.system("cls")
    print(s)
    time.sleep(0.5)
    s = s[1:] + s[0]
     