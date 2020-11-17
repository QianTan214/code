# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        """
        找 middle node of linked list
        """

        # 快慢指针
        
        fast = slow = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        return slow
            