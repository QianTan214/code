# lambda表达式用在复合函数里

def quadratic(a, b, c):
    return lambda x: a*x*x + b*x + c

print(quadratic(1,-1, 2)(5)) # 这种写法
