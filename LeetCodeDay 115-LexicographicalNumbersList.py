class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        intList=[]
        for i in range(1,n+1):
            res.append(str(i))
        for i in sorted(res):
            intList.append(int(i))
        return intList


print(Solution().lexicalOrder(13)) # [1,10,11,12,13,2,3,4,5,6,7,8,9]
print(Solution().lexicalOrder(2))  # [1,2]

