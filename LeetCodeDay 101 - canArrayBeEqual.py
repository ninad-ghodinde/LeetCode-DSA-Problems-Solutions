class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        if sorted(target) == sorted(arr):
            return True
        else:
            return False

print(Solution().canBeEqual([1,2,3,4], [2,4,1,3]))