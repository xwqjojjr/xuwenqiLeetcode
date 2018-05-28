# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        res = p = ListNode(0)
        for i in l:
            temp = ListNode(0)
            temp.val = i
            p.next = temp
            p = temp
        return res.next
            
