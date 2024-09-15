class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1
            

print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)) # [1,2,2,3,5,6]
print(Solution().merge([4,5,6,0,0,0],3,[1,2,3],3)) # [1,2,2,3,5,6]
        