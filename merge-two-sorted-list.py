# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        while l1 != None:
            l.append(l1.val)
            l1 = l1.next
        while l2 != None:
            l.append(l2.val)
            l2 = l2.next
        l.sort()
        l3 = ListNode(l[0])
        p = l3
        for i in range(len(l)-1):
            p.next = ListNode(l[i+1])
            p = p.next
        p.next = None
        return l3


                

            