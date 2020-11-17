"""模"""
%8 
result:0 - 7

"""向上取整"""
(x - 1) // m + 1

"""列表元素相加"""
total = sum((x - 1)//m + 1 for x in nums)

""" 列表元素 """
>>> a = [1]
>>> a[0] # 1
>>> a[:] # [1]
>>> a[:0] # []
>>> a[0:] # [1]

""" bool """

>>> bool([]) # False
>>> bool(None) # False
>>> bool([None]) # True 注意这里


""" is和= """

is比较的是两个整数对象的id值是否相等，也就是比较两个引用是否代表了内存中同一个地址。
==比较的是两个整数对象的内容是否相等，使用==时其实是调用了对象的__eq__()方法。


"""用list构建string"""

chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
name = ''.join(chars)
print(name)  # jackfrued


"""用zip组合键和值来创建字典"""

keys = ['1001', '1002', '1003']
values = ['骆昊', '王大锤', '白元芳']
d = dict(zip(keys, values))
print(d)

"""判断None"""
不要用检查长度的方式来判断字符串、列表等是否为None或者没有元素，
应该用if not x这样的写法来检查它。

"""import语句"""
如果有多个import语句，应该将其分为三部分，
从上到下分别是Python标准模块、第三方模块和自定义模块，
每个部分内部应该按照模块名称的字母表顺序来排列

"""二分法"""
在一个数组中找一个数



"""Linked list"""
找中点：快慢指针
拆分：快慢指针，在慢指针处分为两个链表，node.next = None
找环：快慢指针可以重合则有环


"""二维数组N * N 创建"""
import numpy as np

N = 3
grid = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    grid.append(row)

print(grid)
print(np.matrix(grid)) # 用numpy打印出来的更好看


"""二维数组N * N 创建，游戏board"""
grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def board():
    print("   0, 1, 2")
    for count, row in enumerate(grid):
        print(count, row)
board()

"""遍历四周"""

# 左上到右下
for i in range(2):
    for j in range(2):
        grid[y+i][x+i]

# 中间到四周
for i in range(-1,2):
    for j in range(-1,2):
        grid[y+i][x+i]


"""bfs, dfs"""
1. bfs: 
queue = []
queue.append(start)
visited = set()
visited.add(start)
while queue:
    queue.pop(0)


2. dfs: 
stack = []
stack.append(start)
visited = set()
visited.add(start)


while stack:
    stack.pop()

3. 遍历
for i in range(m):
    for j in range(n):
        grid[i][j]
directions = [(-1, 0), (1, 0),(0, -1), (0, 1)]



"""动态规划"""

与递归相比，没有任何重复计算
动态规划将计算结果保存，并改变计算顺序
空间复杂度：数组大小

动态规划常见题型：
1. 计数：
- 有多少种方式走到右下角
- 有多少种方法选出k个数使得和是sum

2. 求最大最小值：
- 从左上角走到右下角路径的最大数字和
- 最长上升子序列长度

3. 求存在性：
- 取石子游戏，先手是否必胜
- 能不能选出k个数使得和是sum



动态规划四个组成部分
- 确定状态：最优策略中最后一步，化成子问题
- 转移方程
- 初始条件和边界情况： 一般是 f[0] = 0
- 计算顺序：一般从小到达，二维的话从上到下，从左到右

例子：机器人从左上走到右下
- 转移方程： f[i][j] = f[i-1][j] + f[i][j-1]



"""整数是几位数"""
- len(str(n))
- while loop % count 来算


"""查看python安装的库"""

pip freeze

pip list

pydoc modules # cmd中查看

help("modules") # 交互器中查看

>>> import sys # sys模块中查看
>>> sys.modules.keys()


"""查看python安装路径"""

where python # python安装位置