def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        common=set(nums2)
        for num in nums1:
            if num in common:
                return num
        return -1

print(getCommon("self",[1,2,8,12,32,34,43,52,57,62,64,67,71,71,79,81,86,91,93,94],[9,11,12,14,19,25,29,31,38,39,41,42,58,63,66,70,71,73,91,91]))
#print(getCommon("self",[1,2,4,5,6],[2,5,2,1,5]))



            
                     

