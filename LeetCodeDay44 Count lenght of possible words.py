class Solution(object):
    def countCharacters(self, words, chars):
        #print('words:', words)
        finalCtr=0
        for word in words:
            #print('word:',word)
            main=chars
            ctr=0
            for i in range(len(word)):
                if word[i] in main:
                    #print('word[i]:',word[i])
                    main=main.replace(word[i],'',1)
                    ctr+=1
                else:
                    #ctr=0
                    break
                print('chars:',main) 
            if ctr==len(word):
                    finalCtr+=len(word)
                    ctr=0
            
        return finalCtr
#print(Solution().countCharacters(["cat","bt","hat","tree","nin","aan"], "atach"))
print(Solution().countCharacters(["boygirdlggnh"], "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"))