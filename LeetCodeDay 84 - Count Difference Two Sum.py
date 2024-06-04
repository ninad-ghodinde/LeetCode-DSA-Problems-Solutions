class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        left=0 
        right=len(nums)-1
        nums2=list(nums)
        nums2.sort()

        while left<right:
            if abs(nums2[left]-nums2[right])==k:
                ans+=1
                left+=1
            else:
                left+=1
            if (left==right):
                right-=1
                left=0
        return ans
print(Solution().countKDifference([1,2,2,1],1))
print(Solution().countKDifference([1,3],3))
print(Solution().countKDifference([3,2,1,5,4],2))