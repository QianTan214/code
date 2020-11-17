import random

def roll_dice(n=2):
    res = 0
    for _ in range(n):
        res += random.randint(1,6)
    return res



# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))