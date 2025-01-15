class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        ln=len(nums)
        while target > nums[i]:
            if i == ln-1:
                return ln
            i+=1
        return i
        
print(Solution().searchInsert([1,3,5,6], 5)) #2
print(Solution().searchInsert([1,3,5,6], 2)) #1
print(Solution().searchInsert([1,3,5,6], 7)) #4