class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total=numBottles

        while numBottles>=numExchange:
            remainder=numBottles%numExchange
            quotient=numBottles//numExchange
            total+=quotient
            numBottles=remainder+quotient

        return total
            

print(Solution().numWaterBottles(9, 3))  # 13
print(Solution().numWaterBottles(15, 4))  # 19
print(Solution().numWaterBottles(17, 5))  # 21
print(Solution().numWaterBottles(21, 4))  # 27
        