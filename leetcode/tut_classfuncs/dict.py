
class Province:
 
    country = 'China'
 
    def __init__(self, name, count):
        self.name = name
        self.count = count
 
    def func(self, *args, **kwargs):
        print("func")


# 获取类的成员，即：静态字段、方法、
print(Province.__dict__)

"""
结果：
{'__module__': '__main__', 'country': 'China', 
'__init__': <function Province.__init__ at 0x000002AEC64FC9D0>, 
'func': <function Province.func at 0x000002AEC64FCE50>, 
'__dict__': <attribute '__dict__' of 'Province' objects>, 
'__weakref__': <attribute '__weakref__' of 'Province' objects>, 
'__doc__': None}

"""


# 获取 对象obj1 的成员
obj1 = Province('HeBei', 10000)
print(obj1.__dict__)

"""
结果： {'name': 'HeBei', 'count': 10000}
"""