class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        union=[]
        i,j=max(len(nums1),len(nums2)), min(len(nums1),len(nums2))
        print(i,j)       
        for num in nums1:
            if num in nums2:
                union.append(num)
                nums2.remove(num)
        return union

print(Solution().intersect([1,2,2,1],[2,2])) #[2,2]
print(Solution().intersect([4,9,5],[9,4,9,8,4])) #[4,9]