class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        count=0
        left=0
        right=1

        while right < len(nums):
            if nums[left] == nums[right]:
                nums[right] += 1
                count += 1
            elif nums[left] > nums[right]:
                count += nums[left] - nums[right] + 1
                nums[right] = nums[left] + 1
                #count += 1
            left = right
            right += 1

        print(nums)
        return count

#print(Solution().minIncrementForUnique([1,2,2]))
print(Solution().minIncrementForUnique([3,2,1,2,1,7]))