class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        l=left 
        r=right
        left=0
        right=n-1
        sumArr=[]
        sum=0
        index=0
        while (left<= right):
            sum+=nums[left]
            sumArr.append(sum)
            left+=1
            if left>right:
                sum=0
                index+=1
                left=index
            
        sumArr.sort()
        #print(sumArr)
        result=0
        for i in range(l-1,r):
            #print(sumArr[i])
            result+=sumArr[i]
        return result % (10**9 + 7)


print(Solution().rangeSum([1,2,3,4], 4, 1, 5)) # Expected output: 13
print(Solution().rangeSum([1,2,3,4], 4, 3, 4)) # Expected output: 6
print(Solution().rangeSum([1,2,3,4], 4, 1, 10)) # Expected output: 50