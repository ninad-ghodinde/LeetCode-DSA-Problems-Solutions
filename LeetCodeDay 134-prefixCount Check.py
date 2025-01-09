class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ctr=0
        for word in words:
            if word.startswith(pref):
                ctr+=1
        return ctr

        
print(Solution().prefixCount(["mass","as","hero","superhero"],"as")) #1
print(Solution().prefixCount(["mass","ma","hero","superhero"],"ma")) #2
print(Solution().prefixCount(["leetcode","leet"],"code")) #0