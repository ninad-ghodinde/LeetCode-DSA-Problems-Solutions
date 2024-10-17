class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        strnum=str(num)
        newnum=0
        maxNum=num
        for i in range(0,len(strnum)):
            for j in range(i+1,len(strnum)):
                strlist=list(strnum)
                strlist[i],strlist[j]= strlist[j],strlist[i]
                newnum=int("".join(strlist))
                maxNum=max(maxNum,newnum)
        return maxNum

print(Solution().maximumSwap(2736)) #7236
print(Solution().maximumSwap(9973)) #9973