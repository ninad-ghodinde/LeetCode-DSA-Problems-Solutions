
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 , buy2 = float('inf') ,float('inf')
        profit1, profit2 = 0 ,0
        for price in prices:
            buy1 = min(buy1,price)
            profit1 = max(profit1,price-buy1)
            buy2 = min(buy2,price-profit1)
            profit2 = max(profit2,price-buy2)
        return profit2

                    

print(Solution.maxProfit("self",[1,2,5,0,1,6]))
#print(Solution.maxProfit("self",[7,6,4,3,1]))
print(Solution.maxProfit("self",[1,2,3,4,5]))
#print(Solution.maxProfit("self",[7,1,5,3,6,4]))