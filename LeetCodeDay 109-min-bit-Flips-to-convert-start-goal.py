class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        goalBinary = format(goal, 'b')
        startBinary = format(start, 'b')
        #maxDigit = max (len(goalBinary),len(startBinary))
        if (len(goalBinary)) > (len(startBinary)):
            maxDigit = len(goalBinary)
            startBinary = startBinary.rjust( maxDigit,'0')
        else:
            maxDigit = len(startBinary)
            goalBinary = goalBinary.rjust( maxDigit,'0')
        cnt=0
        for i in range(0,maxDigit):
            if startBinary[i] == goalBinary[i]:
                pass
            else:
                cnt+=1
        return cnt

print(Solution().minBitFlips(2,6)) #0010,1010 =>Min bit flips required to got from 2 to 6 is :Ans 1
print(Solution().minBitFlips(2,1)) #2
