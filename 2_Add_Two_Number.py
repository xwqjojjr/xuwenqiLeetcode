class Solution(object):
    def Travel(self,l1):
        a = 0
        flag_a =1
        p  = ListNode(0)
        p = l1
        while(p.val == 0 and p.next != None):
            flag_a = flag_a*10
            p = p.next
        while l1 != None:
           a = a*10+l1.val
           l1 = l1.next
        A=str(a)
        A = A[::-1]
        a = int(A)
        return a*flag_a
    
    def addTwoNumbers(self, l1, l2):
        c = self.Travel(l1)+self.Travel(l2)
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
