class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        timer=0
        while tickets[k]>0:
            for i in range(len(tickets)):
                if tickets[i]>0:
                    tickets[i]-=1
                    timer+=1
                    if tickets[k]==0:
                        break
                    
                
        return timer

print(Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))