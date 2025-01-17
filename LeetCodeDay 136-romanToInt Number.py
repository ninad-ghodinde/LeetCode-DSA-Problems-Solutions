class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ['I','X','C']
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        index=0
        for index in range(0,len(s)-1):
            if val[s[index]] <  val[s[index+1]]:
                sum = sum-val[s[index]]
            else:
                sum = sum + val[s[index]]
        sum+=val[s[len(s)-1]]
        return sum
        

print(Solution().romanToInt('III')) #3
print(Solution().romanToInt('IV')) #4
print(Solution().romanToInt('IX')) #9
print(Solution().romanToInt('LVIII')) #58