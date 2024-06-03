class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    break
        return ans
    

#print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4],6))

        