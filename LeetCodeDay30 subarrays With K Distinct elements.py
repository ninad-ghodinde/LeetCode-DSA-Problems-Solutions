from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """maxlen=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                #print(nums[i:j])
                if len(set(nums[i:j]))==k:
                    #print(nums[i:j])
                    maxlen+=1
        return maxlen"""
        def subarraysWithAtMost(kElem):
            freq = defaultdict(int)
            l = ans = 0

            for r,num in enumerate(nums):
                print("r:",r,"num:",num)
                freq[num]+=1
                while len(freq)>kElem:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                
                ans+=r-l+1
            
            return ans

        return subarraysWithAtMost(k)-subarraysWithAtMost(k-1)
                    
        
                

#print(Solution().subarraysWithKDistinct([1,2,1,2,3],2))
print(Solution().subarraysWithKDistinct([1,2,1,3,4],3))
