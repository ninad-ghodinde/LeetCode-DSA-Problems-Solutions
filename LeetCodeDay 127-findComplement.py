class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binr=bin(num)[2:] # remove the 0b from the binary representation
        strCompliment=""
        for i in binr:
            if i == "0" :
                strCompliment+="1"
            else:
                strCompliment+="0"
        return int(strCompliment,2)

print(Solution().findComplement(5)) #2
print(Solution().findComplement(1)) #0

