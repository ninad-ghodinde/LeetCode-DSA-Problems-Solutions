from collections import defaultdict
class Solution(object):
    def countSubarrays(self, nums, k):
        maxlen=0
        #start=0
        #ocr={}
        for start in range(0,len(nums)):  
            ocr={}          
            for end in range (start, len(nums)):
                if nums[end] not in ocr:
                    ocr[nums[end]]=1
                else:
                    ocr[nums[end]]+=1
                if ocr[nums[end]]>=k:
                    maxlen+=1
                    continue
     
        return maxlen
    
print(Solution().countSubarrays([1,3,2,3,3],2)) #7
                
            