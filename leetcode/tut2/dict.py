# 可以用字典映射 C语言的switch default语句

switch里的default

可以用[]访问value，也可以用.get()的方法

如dict.get(day, "Unknown") # "Unknown是key不存在时的默认值"

get具有容错性，返回默认值"Unknown"

dict.get(day,"Unknown")() # 如果get返回的是个函数，后面加括号就可调用函数



# 下面例子指如果key不存在，则返回get_default这个默认函数，后面加()即调用这个函数

例子：
def get_default():
    return "Unknown"

day_name = dict.get(day, get_default)()


"""
列表推导式
"""
例子：
a = [1,2,3,4,5,6]

b = [i**2 for i in a if i > 3]

def mul(x):
    return x**2

c= map(mul, a)
c = list(c)

print(c)
print(b)


set, dict, tuple也可被推导式


"""
颠倒dict里key和value
"""
例子：
students = {"Tom":18, "Jerry":20}

res = {value: key for key, value in students.items()}
print(res)
# 结果 {18: 'Tom', 20: 'Jerry'}



