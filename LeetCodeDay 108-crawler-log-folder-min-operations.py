class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        cnt=0
        for op in logs:
            if cnt<0:
                cnt=0
            if op =="../":
                cnt-=1
            elif op== "./":
                cnt=cnt
            else:
                cnt+=1
        if cnt<0:
            return 0
        else:
            return cnt

#Min operation required to reach the initial folder
print(Solution().minOperations(["d1/","../","../","../"])) #0
print(Solution().minOperations(["../","d3/","d32/"]))#2