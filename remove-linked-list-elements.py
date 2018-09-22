class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        if not head: return
        while p.next and p.next.val != val: p = p.next
        q = p.next
        if q: p.next = q.next
        else: p.next = None
        if p.next: self.removeElements(p, val)
        return head.next if head.val == val else head