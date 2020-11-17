class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __len__(self):
        return len(self.__dict__) 

a = A()
print(a.__dict__) # a.__dict__表示获取对象a的成员
print(len(a))

"""
结果：
{'a': 1, 'b': 2}
2

"""