"""设计一个生成指定长度验证码的函数"""

"""
random模块的sample和choices函数都可以实现随机抽样。
sample实现无放回抽样，这意味着抽样取出的字符是不重复的；
choices实现有放回抽样，这意味着可能会重复选中某些字符。
这两个函数的第一个参数代表抽样的总体，而参数k代表抽样的数量
"""

# method 1: random.randrange

import random
import string

# all numbers and upppercase and lowercase letters
all_characters = string.digits + string.ascii_letters


def generate_barcode(N = 4):
    res = ""

    for _ in range(N):
        index = random.randrange(len(all_characters)) # 0到字符串长度减1范围
        res += all_characters[index]

    print(res)

generate_barcode()


# method 2: random.choices/random.sample
import random
import string

all_characters = string.digits + string.ascii_letters

def generate_barcode(N = 50):
    return "".join(random.choices(all_characters, k = N))

print(generate_barcode())
