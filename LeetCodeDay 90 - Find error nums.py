class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        uniq=set()
        list2=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                list2.append(i)
            if nums[i-1] in uniq:
                list2.insert(0,nums[i-1])
            else:
                uniq.add(nums[i-1])
        return list2
        
           
print(Solution().findErrorNums([1,2,2,4])) # [2,3]
print(Solution().findErrorNums([2,2])) # [2,1]