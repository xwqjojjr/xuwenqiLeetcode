class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == ")" or s[i] =="]" or s[i] == "}":
                if len(stack) == 0:
                    return False
                if s[i] == ")":
                    if stack.pop() != "(":
                        return False
                if s[i] == "]":
                    if stack.pop() !="[":
                        return False
                if s[i] == "}" :
                    if stack.pop() != "{":
                        return False
                #print stack
            else:
                stack.append(s[i])
                #print stack
        if len(stack) == 0:
            return True      
        else:
            return False
