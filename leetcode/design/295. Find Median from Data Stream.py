# hard
"""
Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""

# method 1: 排序法 

此方法是最简单直接的一个方法，
我们将添加的数保存在数组中，返回中位数时，只需将数组排序，返回中间位置数即可。
slow 15%

class MedianFinder:

    def __init__(self):
        
        """
        initialize your data structure here.
        """
        
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        n = len(self.l)
        if n % 2 == 1:
            return self.l[(n -1)// 2]
        else:
            return (self.l[n//2 -1] + self.l[n//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# method 2：二分查找插入

方法一的缺点在于对数组进行了排序操作，导致时间复杂度较高，假如每次插入一个值前数组已经排好序了呢？
这样我们只需考虑每次将值插在合适的位置即可，所以使用二分查找来找到这个合适的位置，
会将时间复杂度降低到 O(n)

# method 2: bisect.insort_left
def addNum(self, num: int) -> None:  
    bisect.insort_left(self.l, num)

