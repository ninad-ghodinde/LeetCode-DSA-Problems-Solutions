import collections


class Solution(object):
    def findDuplicate(self, nums):
        """for i in nums:
            if nums.count(i)>1:
                return i"""
        #alternate solution for biggger array
        c=[]
        c=set()
        for i in nums:
            if i in c:
                return i
            c.add(i)
            
print(Solution().findDuplicate([3,4,3,2]))