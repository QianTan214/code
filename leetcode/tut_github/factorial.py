""" 计算C(m,n) """

# method 1: define factorial function

def fact (n):
    res = 1
    if n == 0:
        return 1
    while n != 0:
        res = res * n
        n = n - 1
    return res

m = int(input("m: "))
n = int(input("n: "))

result = fact(m) // fact(n) // fact(m-n)
print(result)


""" 计算C(m,n) """

# method 2: for loop 这样不好，代码重复，应该定义一个函数做

# 求m阶乘
m = int(input("m: "))
n = int(input("n: "))

fm = 1
for m in range(1, m+1):
    fm *= m

# 求n阶乘
fn = 1
for n in range(1, n+1):
    fn *= n

# 求m-n阶乘
f_mn = 1
for i in range(1, m-n+1):
    f_mn *= i

res = fm //fn //f_mn

print(res)