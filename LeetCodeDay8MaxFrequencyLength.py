def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unq=set(nums)
        high=[]
        sum=0
        #print(unq)
        for i in unq:
            #print(i,nums.count(i))
            high.append(nums.count(i))
            high.sort(reverse=True)
        #print(max(nums.count(i) for i in unq))
        #print(high )
        for i in unq:
            if nums.count(i) == max(high):
                #print(i)
                sum=sum+nums.count(i)
            else: 
                continue
        return sum

print(maxFrequencyElements(self="", nums=[1,2,2,3]))

