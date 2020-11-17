"""
lt(a, b) 相当于 a < b

le(a,b) 相当于 a <= b

eq(a,b) 相当于 a == b

ne(a,b) 相当于 a != b

gt(a,b) 相当于 a > b

ge(a, b) 相当于  a>= b

"""

class A:

    def __init__(self):
        self.a = 1
        self.b = 2
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True

a = A()
b = A()
print(a == b)

"""
结果：True

"""