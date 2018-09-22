# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import copy
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:return False
        fast = copy(head.next)
        slow = head
        while fast:
            if fast == slow: return True
            else:
                fast = fast.next
                if not fast: return False
                else:
                    fast = fast.next
                    slow = slow.next
        return False
