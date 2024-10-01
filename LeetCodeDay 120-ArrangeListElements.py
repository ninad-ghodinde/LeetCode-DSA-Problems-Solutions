class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        #arr=sorted(arr)
        mp = [0] * k

        # Count occurrences of each remainder
        for x in arr:
            rem = (x % k + k) % k  # Ensure non-negative remainder
            mp[rem] += 1

        # Check pairing conditions
        for i in range(k):
            if i == 0:
                # Remainder 0 must appear in even count
                if mp[i] % 2 != 0:
                    return False
            else:
                # Remainders must match
                if mp[i] != mp[k - i]:
                    return False

        return True
            
print(Solution().canArrange([1,2,3,4,5,10,6,7,8,9],5)) #True
print(Solution().canArrange([1,2,3,4,5,6],7)) #True
print(Solution().canArrange([1,2,3,4,5,6],10)) #False
print(Solution().canArrange([-1,-1,-1,-1,2,2,-2,-2],3)) #False

        