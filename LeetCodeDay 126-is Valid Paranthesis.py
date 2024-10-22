from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        for chr in s:
            if chr == "(" or chr== "[" or chr == "{":
                stack.append(chr)
            elif len(stack)>0:
                if chr == ")" and stack[-1]=="(":
                    stack.pop()
                elif chr == "]"and stack[-1]=="[":
                    stack.pop()
                elif chr == "}"and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False

print(Solution().isValid("()")) # True
print(Solution().isValid("()[]{}")) # True
print(Solution().isValid("(]")) # False