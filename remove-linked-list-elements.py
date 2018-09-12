class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        
        if head == None:
            return
        while p.next != None and p.next.val != val:
            p = p.next
        q = p.next
        if q != None:
            p.next = q.next
        else:
            p.next = None
        if p.next != None:
             self.removeElements(p, val)
        if head.val == val:
            return head.next
        else:
            return head