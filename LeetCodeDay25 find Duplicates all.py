import collections

class Solution(object):
    def findDuplicates(self, nums):
        s=set()
        dups=[]
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                dups.append(i)
        return dups


print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))