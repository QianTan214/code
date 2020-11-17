# 函数式编程
# 尽可能少用for while loop
# 常用三个函数 map filter reduce

# map (function, data)

def double(n):
    return n * 2

l = [1,2,3,4,5]
res = map(double, l)
res = list(res)
print(res)

# .copy()