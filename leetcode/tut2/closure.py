"""闭包"""

python一切皆对象

可以把函数作为参数，传递到另外一个函数里

可以把函数作为另一个函数的return 结果

global 关键字
nonlocal 关键字


例子1：
def curve_pre():
    def curve():
        print("This is curve function")
        pass
    return curve

f = curve_pre()
f() # f是个函数，后面加()就可执行这个函数了

结果
This is curve function



例子2：作用域

a = 10
def f1(x):
    return a * x * x
print(f1(2))

结果
40


# 闭包 = 函数 + 环境变量（函数定义时的外部变量，但不可以是全局变量）
例子3：

def curve_pre():
    a = 25 # a必须在curve函数外部，在内部就不叫闭包了
    def curve(x):
        return a * x * x
    return curve

a = 10 # 外部变量
f = curve_pre()
print(f(2))

结果
100
# a是25， 不受10影响



例子4：

def curve_pre():
    a = 25 # a必须在curve函数外部，在内部就不叫闭包了
    def curve(x):
        return a * x * x
    return curve

a = 10 # 外部变量
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)

print(f(2))

结果
(<cell at 0x000001BA68FDD1C0: int object at 0x00007FFF6C1C3A20>,)
25
100


例子5：

def f1():
    a = 10
    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()

结果
10
20
10



例子6：

def f1():
    a = 10
    def f2():
        a = 20
    return f2

f = f1()
print(f)
print(f.__closure__)

结果：
<function f1.<locals>.f2 at 0x0000027BDD1AD9D0>
None # 不是闭包，因为有局部变量a = 20