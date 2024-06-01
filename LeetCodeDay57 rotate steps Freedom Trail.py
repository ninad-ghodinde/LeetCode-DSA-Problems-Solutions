class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        
        press=0
        round=0
        for i in range(0,len(key)):
            print(ring)
            print(key[i])
            var = self.rotate(ring,key[i])
            print()
            if var[1]=="Clockwise":
                ring = ring[var[0]:]+ring[:var[0]]
                round+=var[0]
                press+=1
            else:
                ring = ring[-var[0]:]+ring[:-var[0]]
                round+=var[0]
                press+=1
            print(ring)
            print(round+press)
        return round+press
        
    def rotate(self,word,char):
        #rev = word[::-1]
        if word[0] == char:
            return 0,"Clockwise"
        right = word[word.index(char):]+word[:word.index(char)]
        left = word[-word.index(char):]+word[:-word.index(char)]
        print(right)
        print(left)
        if right.index(char) <= left.index(char):
            direction="Clockwise"
            print(right.index(char))
            return right.index(char),direction
            
        else:
            direction="Anti-Clockwise"
            print(left.index(char))
            return left.index(char),direction

    

#print(Solution().findRotateSteps("godding", "gd"))
#print(Solution().findRotateSteps("godding", "godding"))
print(Solution().findRotateSteps("abcde", "ade"))

