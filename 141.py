# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        p = q = head
        while (p!=None and q!=None and  q.next!=None):
            p = p.next
            q = q.next.next
            if(p == q):
                return True
        return False
