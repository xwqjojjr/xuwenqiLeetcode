class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        print l
        l.reverse()
        s = ''.join(l)
        return s