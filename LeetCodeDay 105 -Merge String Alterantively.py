class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        final=""
        maxlen= max(len(word1),len(word2))
        for i in range(0,maxlen):
            if (i+1)<=min(len(word1),len(word2)):
                final+=word1[i]+word2[i]
            elif len(word1)>len(word2):
                final+=word1[i]
            else:
                final+=word2[i]
        return final
        


print(Solution().mergeAlternately("abc","pqr"))