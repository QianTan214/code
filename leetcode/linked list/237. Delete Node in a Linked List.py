# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        """
        删除指定节点Node
        
        """


        # 把要删除的node变成下一个node，然后指向下下个node

        node.val = node.next.val
        
        node.next = node.next.next
        
