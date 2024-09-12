class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        cnt=0
        for word in words:
            uniq=set(word)
            for letter in uniq:
                if letter not in allowed:
                    cnt+=1
                    break
            
        return len(words)-cnt
        #another solution
        '''cnt=0
        flag=0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    flag=0
                    break
                else:
                    flag=1
            if flag ==1:
                cnt+=1
        return cnt'''
        
print(Solution().countConsistentStrings("abc",["a","b","c","ab","ac","bc","abc"])) #7
print(Solution().countConsistentStrings ("cad", ["cc","acd","b","ba","bac","bad","ac","d"])) #4