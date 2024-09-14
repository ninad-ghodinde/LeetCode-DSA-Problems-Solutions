class Solution(object):
    def longestSubarrayBitWiseAND(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        final=0
        maxVal=0
        for num in nums:
            if num>maxVal:
                maxVal=num
                cnt=0
                final=0
                ans=max(cnt,final)
            if num==maxVal:
                cnt+=1
                final=max(cnt,final)
            else:
                cnt=0
                final=max(cnt,final)
        return final
            
        
print(Solution().longestSubarrayBitWiseAND([1,2,3,4])) # 1
print(Solution().longestSubarrayBitWiseAND( [1,2,3,3,2,2])) # 2
print(Solution().longestSubarrayBitWiseAND([10,2,2,2,3,3,5,5])) #1