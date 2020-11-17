# *args像是tuple, **kwargs像是dict

"""
题目24：函数参数*arg和**kwargs分别代表什么？
Python中，函数的参数分为位置参数、可变参数、关键字参数、命名关键字参数。
*args代表可变参数，可以接收0个或任意多个参数，当不确定调用者会传入多少个位置参数时，
就可以使用可变参数，它会将传入的参数打包成一个元组。**kwargs代表关键字参数，
可以接收用参数名=参数值的方式传入的参数，传入的参数的会打包成一个字典。
定义函数时如果同时使用*args和**kwargs，那么函数可以接收任意参数

"""

blog1 = "hello"
blog2 = "there"
blog3 = "what is your name?"


def blog_func(title, *args):
    print(title)
    for blog in args:
        print(blog)

blogpage = "My blog"

blog_func(blogpage, blog1, blog2, blog3)

"""
结果：
My blog
hello
there
what is your name?
"""



""" 求和 *args """

def add(*args):
    res = 0
    for val in args:
        res += val
    return res

print(add(1,2,3))
print(add(1,2,3,4))
print(add(1,2,3,4,5))