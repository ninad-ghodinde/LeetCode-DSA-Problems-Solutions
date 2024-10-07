class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''while "AB" in s or "CD" in s:
            if "AB" in s:
                s=s.replace("AB","")
            if "CD" in s:
                s=s.replace("CD","")
        return len(s)'''
        #alteranted solution
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i=="B" and stack[-1]=="A":
                stack.pop()
            elif i=="D" and stack[-1]=="C":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)


#print(Solution().minLength("ACBBD"))
print(Solution().minLength("ABFCACDB"))