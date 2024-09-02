class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        summ=sum(chalk)
        rem=k%summ
        #print(rem)
        if (rem==0):
            return 0
        i=0
        while (rem >= 0):
            rem=rem-chalk[i]
            if (rem>=0):
                i+=1
            else:
                return i
            
print(Solution().chalkReplacer([5,1,5],22)) #0
print(Solution().chalkReplacer([3,4,1,2],25)) #1

            
