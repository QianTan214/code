"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the 
capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dic = collections.OrderedDict()
        self.size = 0 # current size 
        

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.dic.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.dic[key] = value
                self.size += 1
            elif self.size >= self.capacity:
                self.dic.popitem(False)
                self.dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)