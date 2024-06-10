class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count= {0:1}
        total = 0
        res = 0
        remainder=0
        
        for num in nums:
            total += num
            remainder = (total%k+k)%k
            res+= count.get(remainder,0)
            count[remainder] = count.get(remainder,0)+1
        return res

        


print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))