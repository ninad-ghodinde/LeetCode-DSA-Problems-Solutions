class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        for i in nums:
            if i>0:
                s.add(i)
        print(s)
        if len(s)==0:
            return 1
        
        else:
            for i in range(1,len(nums)+2):
                if i not in s:
                    return i

#print(Solution().firstMissingPositive([-1,-2,-3,4,3,2,1]))
print(Solution().firstMissingPositive([2,1]))