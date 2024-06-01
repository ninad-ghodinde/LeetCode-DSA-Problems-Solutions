class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #remainder = 0
        str1=""
        while n!=0:
            remainder = n%2
            str1+=str(remainder)
            n=n//2
        print('str:',str1)
        ctr=0
        for i in range(len(str1)):
            if str1[i]=='1':
                ctr+=1
        #return str1.count('1')
        return ctr
        
        
print(Solution().hammingWeight(10)) # 3