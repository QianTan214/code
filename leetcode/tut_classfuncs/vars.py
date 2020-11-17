print("----是否是实例-------")

from collections import Iterable

print(isinstance([],Iterable))

class A:
    pass
class B(A):
    pass

b = B()
print(isinstance(b,A))
print(isinstance(b,object))


"""
Check if "Hello" is one of the types described in the type parameter:
x = isinstance("Hello", (float, int, str, list, dict, tuple))
"""

print("----是否是子类-------")

class A:
    pass
class B(A):
    pass
print(issubclass(B,A)) # True
print(issubclass(A,B)) # False
print(issubclass(A,object)) # True
print(issubclass(B,object)) # True
"""
issubclass(object, subclass)
object:	Required. An object.
subclass: A class object, or a tuple of class objects
"""


print("----vars-------")

# 看全局
a = 1
b = 2
print(vars()) # k_v
print(dir()) # k


print("----vars类对象-------")

class A:
    c = 1
    d = 2
    def func(self,name):
        self.name = name

print(vars(A))
a = A()
a.func("safely")

print(vars(a))