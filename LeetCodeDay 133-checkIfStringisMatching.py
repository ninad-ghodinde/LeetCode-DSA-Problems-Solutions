class Solution:
    def stringMatching(self, words):
        lst=set()
        index =0
        while index < len(words):
            for i in range(0,len(words)):
                if index == i:
                    continue
                else:
                    if words[index] in words[i]:
                        lst.add(words[index])
            index+=1
        return list(lst)
                    

print(Solution().stringMatching(["mass","as","hero","superhero"])) #["as","hero"]




            
            


        
        