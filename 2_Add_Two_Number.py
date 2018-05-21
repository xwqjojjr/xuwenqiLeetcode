tion for singly-linked list.
class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = 0
        b = 0
        ListNode l = NULL
        while l1 != None:
           #print l1.val
           a = a*10+l1.val
           l1 = l1.next
        while l2 != None:
           #print l2.val
           b = b*10 +l2.val
           l2 = l2.next
        #print a
        #print b
        c = a+b
        while c != 0:
            l.val = c%10
            l = l.next
            c = c/10
        return l
