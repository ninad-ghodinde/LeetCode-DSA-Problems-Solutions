class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
        jobs_dict= zip(difficulty, profit)
        jobs_dict_sorted=sorted(jobs_dict)
        worker.sort()

        print(jobs_dict_sorted)
        print(worker)

        max_profit,index,netProfit=0,0,0
        for work in worker:
            while index<len(difficulty) and work >= jobs_dict_sorted[index][0]:
                max_profit=max(max_profit,jobs_dict_sorted[index][1])
                index+=1
            netProfit+=max_profit
        return netProfit


#Test Cases
#print(Solution().maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))
#print(Solution().maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82,52]))
#print(Solution().maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))
print(Solution().maxProfitAssignment([13,58,37],[4,90,96],[34,73,45]))
#print(Solution().maxProfitAssignment([66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63],[66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77],[61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]))