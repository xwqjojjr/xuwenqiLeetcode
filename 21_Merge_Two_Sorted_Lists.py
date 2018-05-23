# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        p = ListNode(-1)
        res = ListNode(0)
        res.next = l1
        p = res
        while(l1 != None or l2 !=None):
            if(l1 == None):
                p.next = l2
                print "one"
                return res.next
            if(l2 == None):
                p.next = l1
                print "two"
                return res.next
            if(l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
                p = p.next
                print "three"
                continue
            if(l1.val > l2.val):
                p.next= l2
                l2 = l2.next
                p = p.next
                print "four"
                continue
        return res.next
