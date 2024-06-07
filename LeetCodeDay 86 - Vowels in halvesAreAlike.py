class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #vowels=set('a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowels = set("aeiouAEIOU")
        split1=s[:len(s)//2]
        split2=s[len(s)//2:]
        count1=0
        count2=0
        for i in split1:
            if i in vowels:
                count1+=1
        for i in split2:
            if i in vowels:
                count2+=1
        if(count1==count2):
            return True
        else:
            return False

print(Solution().halvesAreAlike("book"))
print(Solution().halvesAreAlike("textbook"))
        