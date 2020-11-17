# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        """
        Given a linked list, 
        return the node 在环开始的地方. 如没有环, return null.

        """

        # a + n(b+c) + b = 2 * (a+b)
        
        # a = c +(n-1)(b+c)
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: # 快慢指针相遇，相遇点是slow指针的位置
                slow2 = head # 一个新指针slow2，指向head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow # slow和slow2相遇的话返回slow
        return None # 如果链表不存在环，则直接退出，有环的话一定会一直转下去