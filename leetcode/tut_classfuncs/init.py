""" 
__init__构造方法，通过类创建对象时，自动触发执行

"""

class Student:

    def __init__(self, name, *age):
        self.name = name
        self.age = age
    
stu = Student("Tom")

print(stu.name)

"""
结果: Tom

"""