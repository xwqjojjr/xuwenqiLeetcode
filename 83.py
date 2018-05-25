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
        dummy = ListNode(0)
        dummy.next = q = head
        while head.next :
            head = head.next
            if q.val != head.val:
                q.next = head
                q = q.next
                print q.val
        q.next = None
        return dummy.next
                
                
