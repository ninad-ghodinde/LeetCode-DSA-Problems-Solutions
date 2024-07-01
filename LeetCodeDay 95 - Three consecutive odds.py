class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag=0
        for num in arr:
            if num%2==1:
                flag+=1
            else:
                flag=0
            if flag==3:
                return True
        return False
        
        
print(Solution().threeConsecutiveOdds([2,6,4,1])) #False
print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])) #True