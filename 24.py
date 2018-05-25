# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
       
    def swapPairs(self, head):
        
        if(head==None or head.next==None):
            return head
        
        prev=None
        p1=head
        p2=head.next
        p3=head.next.next
        head= p2
        while p1 and p1.next:
            p2.next=p1
            p1.next=p3
            if prev:
                prev.next=p2
            prev=p1
            p1=p3
            if p3:
                p2=p3.next
            if p2:
                p3=p2.next
            
        return head
