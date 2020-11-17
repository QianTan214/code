""" 树 """

树相当于对链表的扩充，树是二维的

""" 术语 """

节点的度：一个节点有几个子树

树的度：最大节点的度

叶节点：度为0的节点

节点的层

树的深度/高度：树中节点的最大层次

""" 树的种类 """

无序树

有序树：二叉树，霍夫曼树，B树

二叉树：每个节点最多含有两个子树的树

二叉树分类：完全二叉树，满二叉树，平衡二叉树，排序二叉树

完全二叉树：比如有n层，第1到第(n-1)层与满二叉树一样，第n层最后一个节点前边都挂满了节点

二叉排序树binary search tree， 左小右大 （二分查找的应用）


""" 树的存储 """

顺序存储，用数组

链式存储


""" 树的应用场景 """

xml, html
路由协议
mysql数据库索引
经典的AI算法

""" 树的遍历 """
bfs

dfs：先序，中序，后序遍历



""" 树的代码实现 """

"""节点类"""

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

"""树的类"""

class Tree:
    def __init__(self):
        self.root = None

    # 树添加节点
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        q = []
        q.append(self.root)  
        while q:    
            cur_node = q.pop(0)
            if cur_node.l is None:
                cur_node.l = node
                return
            else:
                q.append(cur_node.l)
            if cur_node.r is None:
                cur_node.r = node
                return   
            else:
                q.append(cur_node.r)
    
    # 广度遍历
    def bfs(self):
        if self.root is None:
            return 
        q = []
        q.append(self.root)
        while q:
            cur_node = q.pop(0)
            print(cur_node.val, end = " ")
            if cur_node.l is not None:
                q.append(cur_node.l)
            if cur_node.r is not None:
                q.append(cur_node.r)

    # 先序遍历(递归)
    def preorder(self, node):
        if node is None:
            return
        print(node.val, end = " ")
        self.preorder(node.l)
        self.preorder(node.r)


    # 中序遍历(递归)
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.l)
        print(node.val, end = " ")
        self.inorder(node.r)


    # 后序遍历(递归)
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.l)
        self.postorder(node.r)
        print(node.val, end = " ")





             
tree = Tree()
tree.add(0)
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.bfs() # 0 1 2 3 4 5 6 7 8 9
print(" ")
tree.preorder(tree.root) # 0 1 3 7 8 4 9 2 5 6
print(" ")
tree.inorder(tree.root) # 7 3 8 1 9 4 0 5 2 6
print(" ")
tree.postorder(tree.root) # 7 8 3 9 4 1 5 6 2 0
print(" ")