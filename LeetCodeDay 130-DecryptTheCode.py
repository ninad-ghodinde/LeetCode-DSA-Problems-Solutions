class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0]*len(code)
        if k==0:
            return result
        start =1
        end = k
        sum = 0

        if k<0:
            start = len(code) - abs(k)
            end = len(code) - 1
        
        for i in range (start, end+1):
            sum += code[i]
        for i in range(len(code)):
            result[i] = sum
            sum -= code[start % len(code)]
            sum += code[(end+1) % len(code)]
            start +=1
            end +=1
        return result

print(Solution().decrypt([5, 7, 1, 4], 3))
        