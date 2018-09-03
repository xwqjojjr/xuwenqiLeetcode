class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mmax =0
        for i in range(len(s)):
            j = i
            for j in range(len(s)):
                if s[j] not in s[i:j]:
                    #print "s[j] = ",s[j],"s[i,j]=",s[i:j]
                    if j-i+1 > mmax:
                        mmax = j-i+1
                    if mmax == 95:
                        return mmax
                if s[j] in s[i:j]:
                   # print mmax
                    break
            count =0
        return mmax
