import collections
def customSortString(self, order, s):
        com=[]                  
        
        print("new code")       
        count=collections.Counter(s)
        print(count)
        for i in order:
                if i in count.keys():
                        print(i)
                        com.append(i*count.pop(i,0))
        print(count)
        for char,cnt in count.items():
                    com.append(char*cnt)
        print(com)
        return ''.join(com)
print(customSortString("self","cba","abcd")) #kqeep
                        
                        
