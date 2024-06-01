
def mergeAlternately(self, word1: str, word2: str) -> str:
        counter=""
        final=""
        if (word1.__len__() >= word2.__len__()):
                counter = word1
        else:
                counter = word2
        #print(counter.__len__())
        #print(counter[0])
        #print(counter[1])
        for i in range(counter.__len__()):
            if(i >= word1.__len__()):
                final = final + word2[i]
            elif(i >= word2.__len__()):
                    final = final + word1[i]
            else:
                final=final+word1[i]+word2[i]       
        #print(final)
        return final
        


mergeAlternately("self", "abcd", "pqhr")
