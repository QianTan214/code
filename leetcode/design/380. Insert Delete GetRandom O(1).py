"""
Implement the RandomizedSet class:

bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class 
with each function works in average O(1) time?
"""

# dict + list解法
import random

class RandomizedSet:
  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 需要一个list和一个dictionary  
        self.list = [] 
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val not in self.dic:
            return False
        
        last, index = self.list[-1], self.dic[val]
        self.list[index], self.dic[last] = last, index
        del self.dic[val]
        del self.list[-1]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:

obj = RandomizedSet()

print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())

"""
结果：
True
False
True
1 or 2
"""