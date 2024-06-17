class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i=0
        arr=[]
        
        while i*i<=c:
            arr.append(i*i)
            i+=1
        left=0
        right=len(arr)-1
        while(left<=right):
            if arr[left]+arr[right]==c:
                print(arr[left],arr[right])
                return True
            if arr[left]+arr[right]>c:
                right-=1
            else:
                left+=1
        return False
        

print(Solution().judgeSquareSum(8))
print(Solution().judgeSquareSum(1))