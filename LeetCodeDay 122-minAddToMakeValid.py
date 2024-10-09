class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open=0
        close=0
        ctr=0
        for i in s:
            if i=="(":
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    close+=1
        return open+close
    
    """alternate solution"""
    """
    stack=[]
        for chr in s:
            if len(stack)==0:
                stack.append(chr)
            elif stack[-1]=="(" and chr==")":
                stack.pop()
            else:
                stack.append(chr)
        return len(stack)
    """
                  
print(Solution().minAddToMakeValid("())")) #1
print(Solution().minAddToMakeValid("()))((")) #4