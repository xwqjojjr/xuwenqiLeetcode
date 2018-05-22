class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = 0
        b = 0
        flag_a = 1
        flag_b = 1
        p  = ListNode(0)
        p = l1
        while(p.val == 0 and p.next != None):
            flag_a = flag_a*10
            p = p.next
        p  = ListNode(0)
        p = l2
        while(p.val == 0 and p.next != None):
            flag_b = flag_b*10
            p = p.next
            
        while l1 != None:
           a = a*10+l1.val
           l1 = l1.next
        while l2 != None:
           b = b*10 +l2.val
           l2 = l2.next
        #print a
        #print b
        A=str(a)
        B=str(b)
        A = A[::-1]
        B = B[::-1]
        a = int(A)
        b = int(B)
        c =a*flag_a+b*flag_b
        #print a ,b
        ll = ListNode(0)
        p  = ListNode(0)
        p = ll
        #print c % 10
        while c >=10:
            temp = ListNode(0)  
            p.val = c % 10  
            p.next = temp 
            p = temp  
            c = c / 10 
            #print c
            #print p.val
        p.val = c %10
        return ll
