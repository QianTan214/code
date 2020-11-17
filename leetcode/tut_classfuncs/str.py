"""
__str__

如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。

"""

class Foo:
    
    def __str__(self):
        return "Hello"


obj = Foo()
print(obj)

"""
结果：Hello
"""


"""
str函数或者print函数--->obj.__str__()
repr或者交互式解释器--->obj.__repr__()
如果__str__没有被定义,那么就会使用__repr__来代替输出
注意:这俩方法的返回值必须是字符串,否则抛出异常

"""