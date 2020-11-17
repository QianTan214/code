"""
Given a stream of integers and a window size, 
calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3)
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

# 双向队列double-ended queue
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.q = deque()
        self.count = 0
        self.sum = 0

    def next(self, val):
        self.count += 1
        self.q.append(val)
        tail = self.q.popleft() if self.count > self.size else 0
        self.sum = self.sum - tail + val
        return self.sum / min(self.count, self.size)

obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))

"""
结果：
1.0
5.5
4.666666666666667
6.0
"""