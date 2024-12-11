class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        wordList = split(sentence)
        for i in range(0,len(wordList)):
            if wordList[i].startswith(searchWord):
                return i+1
        return -1

        
        