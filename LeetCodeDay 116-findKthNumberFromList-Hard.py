class Solution(object):
    def countSteps(self,curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
    
    def findKthNumber(self, n, k):
        curr = 1
        while k > 1:
            steps = self.countSteps(curr, n)
            if steps < k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr



print(Solution().findKthNumber(13,2)) # 10
print(Solution().findKthNumber(13,3)) # 11


