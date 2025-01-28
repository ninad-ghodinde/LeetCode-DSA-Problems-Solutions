class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lists=s.split()
        return len(lists[-1])


print(Solution().lengthOfLastWord("Hello World")) #5
print(Solution().lengthOfLastWord("a ")) #1