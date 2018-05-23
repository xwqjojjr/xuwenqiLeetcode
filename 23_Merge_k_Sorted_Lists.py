# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = ListNode(0)
        res = ListNode(0)
        res.next = p
        temp = ListNode(0)
        l = []
        for i in lists:
            temp = i
            while temp != None:
                l.append(temp.val)
                temp = temp.next
        l.sort()
        print l
        for k in l:
            print k
            q= ListNode(k)
            p.next = q
            p = p.next
        return res.next.next
