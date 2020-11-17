# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # 创建dummy节点, cur指针
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next: # 如果不是最后一个节点
        
            if cur.next.val != val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return dummy.next

