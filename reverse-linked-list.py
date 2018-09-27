# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        if not head: return
        while head:
            l.append(head.val)
            head = head.next
        l = l[::-1]
        n = ListNode(l[0])
        p = n
        for i in range(1, len(l)):
            p.next = ListNode(l[i])
            p = p.next
        p.next = None
        return n
