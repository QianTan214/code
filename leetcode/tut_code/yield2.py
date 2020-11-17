"""
说一下，为什么用这个生成器，是因为如果用List的话，会占用更大的空间，
比如说取0,1,2,3,4,5,6............1000
"""


def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)

"""
结果:
1
2
3
4
5
6
7
8
9
10

"""