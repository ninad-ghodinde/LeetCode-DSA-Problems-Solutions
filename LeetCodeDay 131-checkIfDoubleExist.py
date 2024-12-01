class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        visited =[]
        for num in arr:
            if num*2 in visited or (num%2 ==0 and num//2 in visited):
                return True
            else:
                visited.append(num)
        return False
        
        """
        #Alternate Solution
        if sum(arr) == 0:
            return True
        for i in range (0,len(arr)):
            for j in range (0,len(arr)):
                if i == j:
                    continue
                if arr[i] == 2*(arr[j]):
                    return True
        return False"""

print (Solution().checkIfExist([10,2,5,3]))
print (Solution().checkIfExist([7,1,14,11]))