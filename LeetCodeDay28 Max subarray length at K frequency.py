class Solution(object):
    def maxSubarrayLength(self, nums, k):
        #result_occurrences = {i:nums.count(i) for i in nums}
        maxlen=0
        start=0
        ocr={}
        #print(result_occurrences)

        for end in range(0,len(nums)):
            print(start,end,maxlen)
            if nums[end] not in ocr:
                ocr[nums[end]]=1
            else:
                ocr[nums[end]]+=1
                
            while ocr[nums[end]]>k:
                ocr[nums[start]]-=1
                start+=1
        
            maxlen=max(maxlen,end-start +1)
            print(start,end,maxlen)


        


        return maxlen

            
                
               

print(Solution().maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
#print(Solution().maxSubarrayLength([5,5,5,5,5,5,5], 4))
#print(Solution().maxSubarrayLength([1,4,4,3], 1))

#print(Solution().maxSubarrayLength([1], 1))