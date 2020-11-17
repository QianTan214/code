"""枚举"""

from enum import Enum
# 枚举就是个类，枚举类和普通类不一样,普通类数值可更改，且可以有相同数值。

# 枚举下定义的类型不能被更改
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)
print(VIP.YELLOW.name)
print(VIP.YELLOW.value)

"""
结果: 
VIP.YELLOW
YELLOW
1
"""

# VIP.YELLOW = 6 会报错，不可更改

for v in VIP:
    print(v)

"""
结果
VIP.YELLOW
VIP.GREEN
VIP.BLACK
VIP.RED
"""