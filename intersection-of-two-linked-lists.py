# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA_len = 0
        headB_len = 0
        p1 = headA
        p2 = headB
        result = None
        while p1 != None:
            headA_len += 1
            p1 = p1.next
        while p2 != None:
            headB_len += 1
            p2 = p2.next
        count = abs(headA_len - headB_len)
        n = 0
        while n < count:
            if headA_len > headB_len:
                headA = headA.next
            if headB_len > headA_len:
                headB = headB.next
            n += 1
        if headA == None and headB == None:
            return None
        elif headA == None or headB == None:
            return None
        else:
            pass
        while headA != None and headB != None:
            if headA.val == headB.val:
                result = headA
                return result
            headA = headA.next
            headB = headB.next
        return None
        