
def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        if (len(nums)==1):
            if nums[0]==goal:
                return 1
            else:
                return 0
        count=0
        for i in range(0,len(nums)):
            print("i",i)
            sum=0
            for j in range(i,len(nums)): 
                print("j",j)
                sum=sum+nums[j]
                print("sum",sum)
                if sum==goal:
                     count+=1
                if (sum>goal):
                    break
        return count

print(numSubarraysWithSum("self",[1,0,1,0,1],2)) #4
#print(numSubarraysWithSum("self",[0,0,0,0,0],0)) #4