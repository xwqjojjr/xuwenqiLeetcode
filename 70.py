class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        f1=1
        f2=1
        while i<n:
            f1, f2 = f2,f1+f2
            i+=1
        return f2