"""__doc__表示类的描述信息"""


class Student:

    """描述类信息"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

stu = Student("Tom", 17)
print(stu.__doc__)
print(Student.__doc__)

"""
结果：
描述类信息
描述类信息
"""