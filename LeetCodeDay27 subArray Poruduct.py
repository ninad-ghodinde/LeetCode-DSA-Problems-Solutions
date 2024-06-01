class Solution(object):
    def subArrayproduct(self,nums,k):
        """
        if len(nums) == 0 or k<=1:
                return 0
        counter=0
        for i in range(len(nums)):
            mul=1
            for j in range(i,len(nums)):
                    mul=mul*nums[j]
                    if mul>=k:
                        break
                    counter+=1
        return counter"""
        
        """alternate solution"""
        if k<=1:
            return 0
        counter=0
        right=0
        left=0
        mul=1
        while(right < len(nums)):
            mul=mul*nums[right]
            while(mul>=k):
                mul=mul/nums[left]
                left+=1
            counter=counter+ right - left + 1
            right+=1
        return counter
   
print(Solution().subArrayproduct([10,5,2,6],100))
#print(Solution().subArrayproduct([1,2,3],0))   
        
