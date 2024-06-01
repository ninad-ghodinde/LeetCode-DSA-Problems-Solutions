class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt=s.count('1')
        total=len(s)
        final=""
        if cnt==0:
            return '0'
        else:
            for i in range (0,total):
                if i==total-1:
                    final=final+"1"
                    break
                else:
                    if cnt>1:
                        final=final+"1"
                        cnt=cnt-1
                    else:
                        final=final+"0"
        return final
    
print(Solution().maximumOddBinaryNumber("100100100")) #100100000
print(Solution().maximumOddBinaryNumber("0101")) #1001
print(Solution().maximumOddBinaryNumber("0000")) #1001
                