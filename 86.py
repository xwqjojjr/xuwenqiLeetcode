# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 =ListNode(0)
        h2 = l2 =ListNode(0)
        
        while head:
            print head.val
            if head.val < x:
                l1.next = head
                l1 = head
            else:
                l2.next = head
                l2 = head
            head = head.next
            
        l1.next = h2.next
        l2.next = None
        
        return h1.next
        
