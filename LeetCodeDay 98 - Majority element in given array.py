class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #counts={i:count for i in nums if (count:=nums.count(i))>len(nums)/2}
        counts={i:count for i in set(nums) if (count:=nums.count(i))>len(nums)/2}
        return counts.popitem()[0]

print(Solution().majorityElement([3,2,3]))  # 3
print(Solution().majorityElement([2,2,1,1,1,2,2]))  # 2