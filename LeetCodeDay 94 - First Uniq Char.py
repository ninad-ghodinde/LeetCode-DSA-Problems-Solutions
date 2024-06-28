import collections as Collection
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts=Collection.Counter(s)
        print(counts)

        for key,value in counts.items():
            if value==1:
                return s.index(key)
        return -1



print(Solution().firstUniqChar("loveleetcode")) #2
print(Solution().firstUniqChar("leetcode")) #0
print(Solution().firstUniqChar("aabb")) #-1
print(Solution().firstUniqChar("dddccdbba")) #8