class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        uncommonWords={}
        for word in s1.split():
            if word in uncommonWords:
                uncommonWords[word]+=1
            else:
                uncommonWords[word]=1
        for word in s2.split():
            if word in uncommonWords:
                uncommonWords[word]+=1
            else:
                uncommonWords[word]=1
        result=[]
        for key,val in uncommonWords.items():
            if val==1:
                result.append(key)
        return result
        
print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour")) # ["sweet","sour"]
print(Solution().uncommonFromSentences("apple apple", "banana"))  # ["banana"]