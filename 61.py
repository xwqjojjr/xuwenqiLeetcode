# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        count = 1
        p = head
        while p.next:
            p = p.next
            count += 1
        p.next = head
        print k,count
        step = count - k%count
        res = dummy = ListNode(0)
        p = head
        res.next = p
        for i in range(step):
            p = p.next
            res = res.next
        res.next = None
        return p
        
