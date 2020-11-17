""" 
__module__ 表示当前操作的对象在哪个模块

__class__ 表示当前操作的对象的类是什么

"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
stu = Student("Tom", 17)

print(stu.__module__)
print(stu.__class__)

"""
结果：
__main__
<class '__main__.Student'>

"""