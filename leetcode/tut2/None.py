"""
None
"""

None不等于(),{},[],False,0

None的类型是NoneType, False是bool类型


比较值 ==， 比较类型 is

例子1：

a = []

if not a:
    print("S")
else:
    print("F")


if a is None:
    print("S")
else:
    print("F")

# 结果 S, F
# 因为None不是[]
# 最好不要用if a is None，就用if a, if not a 就好了



"""
if 类的实例化
"""

例子2：
class Test():
    pass

test = Test()

if test: # bool(test)是True
    print("S")

结果S 


例子3：
class Test():
    def __len__(self): 
        return 0 # 如果不是0，则True

test = Test()

if test: # bool(test) 是False
    print("S")
else:
    print("F")

结果F 


例子4：

class Test():
    def __bool__(self):
        return False
    def __len__(self):
        return 8

print(len(Test())) #如果Test类里没有__len__方法的话会报错
print(bool(Test()))

结果
8
False


例子5：

class Test():
    def __bool__(self):
        print("bool called")
        return False # 不可以写0，只能写True/False
    def __len__(self):
        print("len called")
        return True


print(bool(Test())) # 结果受__bool__影响，不受__len__影响了,因为__len__没有被执行

结果
bool called
False
