"""水仙花数 范围 100 - 1000"""
# 1**3 + 5**3 + 3**3 = 153

# method 1: 
for num in range(100,1000):
    tmp = num
    res = 0
    while num != 0:
        d = num % 10
        res = res + d ** 3
        num = num // 10
    if res == tmp:
        print(res)

# method 2: 
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)