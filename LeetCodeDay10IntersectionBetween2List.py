def intersection(self, nums1, nums2):
    com=[]
    for i in nums2:
        if i in nums1:
            com.append(i)
    com=set(com)
    return list(com)


print(intersection("self",[1,2,2,1],[2,1,2]))
        