
# use list to implement stack and queue

"""栈，也叫栈堆"""

stack []

顺序表和链表都可以表示栈

栈描述的是操作，只能在一端操作。表描述的是数据怎么存放

如果用单链表表示stack，在头部插入和删除。
如果用list表示stack，在尾部插入和删除。
如果反过来，复杂度就是O(n)了
self.list.append(data)
self.list.insert(0, data)


栈的应用：缓冲区、括号匹配、接迷宫



"""队列"""

queue []
一端添加，一端获取

enqueue入队：从尾部/头部增加一个元素
dequeue出队：从尾部/头部删除一个元素

peek：查看队列最前端的元素
isFull：查看队列是否满了
isEmpty：查看队列是否为空



"""双向队列"""

deque []
双端都可添加，双端都可获取



# create a custom stack

class Stack:
    def __init__(self):
        self.__s = []

    def push(self, data):
        self.__s.append(data)

    def pop(self):
        return self.__s.pop()

    def peek(self):
        return self.__s[-1]

s = Stack()
s.push(5)
s.push(15)
s.push(25)

print(s.peek())

element = s.pop()
print(element)



# create a custom queue

class Queue:
    def __init__(self):
        self.__s = []

    def enqueue(self, data):
        self.__s.append(data) # 二选一，看应用是出队还是入队频繁
        self.__s.insert(0, data) 

    def dequeue(self):
        return self.__s.pop(0) # 二选一，看应用是出队还是入队频繁
        return self.__s.pop() 

    def is_Empty(self):
        return self.__s == []

    def size(self):
        return len(self.__s)



# create a custom deque

class Deque:
    def __init__(self):
        self.s = []

    def enqueue(self, data):
        self.s.append(data) # 二选一
        self.s.insert(0, data)

    def dequeue(self):
        return self.s.pop() # 二选一
        return self.s.pop(0)

    def is_Empty():
        return self.s == []

    def size(self):
        return len(self.s)



