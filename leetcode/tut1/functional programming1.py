# 分数化简: 先求两个数最大公约数，再用两个数分别处以最大公约数

# 求最大公约数gcd
# 辗转相除法
# jupyter notebook里, 在section里直接大%%time就可以查看代码运行时间
# random.randint(1, 1000)

from multiprocessing import Pool
import random
import time

def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

# print(gcd(9,12))


# 化简分数
def simplify(pair):
    n1 = pair[0]
    n2 = pair[1]
    m = gcd(n1, n2)
    return (int(n1/m), int(n2/m))

# 源数据
# 在 1 - 1000里取分母和分子, 一共10000个分数
data = [(random.randint(1,1000), random.randint(1,1000)) for _ in range(10000)]

# data = [(1,5),(3,9),(2,4),(6,18)]

# 用for在[]里
"""
res = [simplify(v) for v in data]
"""

# 用函数式编程map函数
"""
res = list(map(simplify, data))
print(res)
"""

# 数据很大时用map运行时间会加快

t1 = time.time()
p = Pool(2) # 开2条进程
res1 = p.map(simplify, data)
t2 = time.time()
print(t2-t1)
