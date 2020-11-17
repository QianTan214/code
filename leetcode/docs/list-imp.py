"""线性表：list 和 linked list"""

"""顺序表：连续存储"""

插入元素：
尾端加入元素O(1)

保序插入元素最坏O(n)

非保序插入元素O(1) -- 不常见


删除元素：
尾端删除元素O(1)

保序删除元素最坏O(n)

非保序删除元素O(1) -- 不常见


python中两种顺序表，list 和 tuple
python中的list是动态顺序表，元素存储区可扩充


"""链表：不连续存储"""

保存数据，保存下一个节点的地址（数据区，指针区/链接区）

还需要一个保存第一个节点（头节点）位置的指针

尾节点链接区指向空None

*************************************************************
python中,a = 10,a表示一块内存，内存中存储10的地址，a中并没有保存10
所以a也可以等于一个函数，如 a = def f(): 
a可以等于任何东西，相当于改变a的指向
*************************************************************


"""链表和顺序表的时间复杂度对比"""

访问元素：O(n), O(1)
头部插入：O(1), O(n)
尾部插入：O(n), O(1)
中间插入：O(n), O(n)

链表每个节点占用空间大了，因为要存储指针


"""单向循环链表"""

尾节点指向头节点
如果链表只有一个节点，则节点指向它自己



**********************************************************************

"""单向链表代码实现"""

"""节点类"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # next是下一个节点的标识

# python里的tuple也能实现节点(data, None)


"""单链表类"""

class SingleLinkedList:

    def __init__(self, node = None): # 默认一开始无节点，head指向None
        self.__head = node  # 私有head，指针

    def is_empty(self):
        return self.__head == None # head指向None链表就是空

    def length(self):
        cur = self.__head # cur指针/游标用来遍历节点
        count = 0
        while cur != None: # 或者cur.next != None, 但count初始值会变
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self.__head
        while cur != None: # 如果写cur.next != None,会丢掉尾节点
            print(cur.data, end = " ")
            cur = cur.next
        print()  

    def add(self, data): # data指具体数据，不是节点，只要数据进来就好，我们写的函数会自动封装成节点
        # 链表头部添加元素，头插法
        node = Node(data)
        node.next = self.__head
        self.__head = node

    def append(self, data): # data指具体数据，不是节点，只要数据进来就好，我们写的函数会自动封装成节点
        # 链表尾部添加元素，尾插法
        node = Node(data) # 先定义一个节点
        if self.__head == None: # 或者if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, data):
        """param pos 初始 0"""
        if pos < 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            node = Node(data)
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1 
                pre = pre.next
            node.next = pre.next
            pre.next = node

    # 用两个指针         
    def remove(self, data): # 删除第一个出现的，如果有重复
        cur = self.__head
        pre = None
        while cur != None:
            if cur.data == data:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        return False

    def search(self, data):
        cur = self.__head
        while cur != None:
            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False

ll = SingleLinkedList()

print(ll.is_empty())

print(ll.length())

ll.append(1)

print(ll.is_empty())

print(ll.length())

ll.append(2)
ll.add(8)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(-1, 9)
ll.insert(3, 100)
ll.insert(10, 200)
ll.traverse()
ll.remove(100)
ll.traverse()
ll.remove(9)
ll.traverse()
ll.remove(200)
ll.traverse()

"""
True
0
False
1
9 8 1 100 2 3 4 5 6 200
9 8 1 2 3 4 5 6 200
8 1 2 3 4 5 6 200
8 1 2 3 4 5 6
"""




*****************************************************************
""" 单向循环链表代码实现 """

"""节点类"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None # next是下一个节点的标识

# 节点python里的tuple也能实现(val, None)


"""单向循环链表类"""

class SingleCyclicLinkedList:

    def __init__(self, node = None): 
        self.__head = node  
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None 

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head 
        count = 1
        while cur.next != self.__head: 
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        if self.is_empty():
            return 
        cur = self.__head
        while cur.next != self.__head:
            print(cur.val, end = " ")
            cur = cur.next
        print(cur.val)  

    def add(self, data): 
        node = Node(data)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, data): 
        node = Node(data) 
        if self.__head == None:
            self.__head = node
            node.next = node

        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, data):
        """param pos 初始 0"""
        if pos < 0:
            self.add(data)
        elif pos > self.length() - 1:
            self.append(data)
        else:
            node = Node(data)
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1 
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, data): 
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.val == data:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.val == data:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, data):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.val == data:
                return True
            else:
                cur = cur.next
        if cur.val == data:
            return True
        return False

ll = SingleCyclicLinkedList()

print(ll.is_empty())

print(ll.length())

ll.append(1)

print(ll.is_empty())

print(ll.length())

ll.append(2)
ll.add(8)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(-1, 9)
ll.insert(3, 100)
ll.insert(10, 200)
ll.traverse()
ll.remove(100)
ll.traverse()
ll.remove(9)
ll.traverse()
ll.remove(200)
ll.traverse()

"""
True
0
False
1
9 8 1 100 2 3 4 5 6 200
9 8 1 2 3 4 5 6 200
8 1 2 3 4 5 6 200
8 1 2 3 4 5 6
"""
