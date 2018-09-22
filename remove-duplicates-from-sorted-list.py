# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        if not head: return
        while head:
            l.append(head.val)
            head = head.next
        l = list(set(l))
        l.sort()
        n = ListNode(l[0])
        p = n
        for i in range(len(l)-1):
            p.next = ListNode(l[i+1])
            p = p.next
        p.next = None
        return n
