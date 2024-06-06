class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        while hand:
            first=hand[0]
            for i in range(groupSize):
                if first+i in hand:
                    hand.remove(first+i)
                else:
                    return False
        return True

print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8],3))
print(Solution().isNStraightHand([1,2,3,4,5],4))