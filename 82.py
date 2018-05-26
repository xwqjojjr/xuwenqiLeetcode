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
        if head == None:
            return head
        if head.next == None:
            return head
        res = dummy  = ListNode(0)
        q = ListNode(0)
        q.next = p = head
        if(q.next.val != p.next.val):
            res.next = ListNode(0)
            res = res.next
            res.val = q.next.val
        p = p.next
        q = q.next
        while p.next :
            if(q.val!=p.val and p.val != p.next.val):
                res.next =  ListNode(0)
                res = res.next
                res.val = p.val
            q = q.next
            p = p.next
        if(q.val != p.val):
            res.next =  ListNode(0)
            res = res.next
            res.val = p.val
        return dummy.next
            
                
            
