"""
如果我们只在双向队列的一端取数据，另一端存数据，那么就实现了先进先出（
first-in-first-out，FIFO）的单向队列。
如果我们只在双向队列的一端存数据和取数据，另一端不操作数据，那么就是实现了栈。
"""

from collections import deque
d = deque("abc")
print(d) 
# deque(['a', 'b', 'c'])

for i in d:
    print(i)
# a b c

d.append("d")
print(d)
# deque(['a', 'b', 'c', 'd'])

d.appendleft("e")
print(d)
# deque(['e', 'a', 'b', 'c', 'd'])

d.pop()
print(d)
# deque(['e', 'a', 'b', 'c'])

d.popleft()
print(d)
# deque(['a', 'b', 'c'])

print(d[0]) # a
print(d[-1]) # c

d.extendleft("g")
print(d)
# deque(['g', 'a', 'b', 'c'])

print("c" in d) # True

d.clear()
print(d)
# deque([])

# 可以把一个列表转为deque
ls = [1,2,3]
d = deque(ls)
print(d)
# deque([1, 2, 3])

print(d.count(3))
# 1


# 只取后两个元素，可以实现打开文件时只取后面几行
print(deque(ls,2)) 
# deque([2, 3], maxlen=2)