def findJudge(self, n, trust):

    print(len(trust))
    found=1
    for j in range(1,n+1):
            print("j",j)
            for i in range(0, len(trust)):
                print("i",i)
                if j == trust[i][0]:
                    print("j",j)
                    found=1
                    break
                else:
                    print("return j",j)
                    found=found+1
                    continue
    if found ==1:
         return -1
    else:
         return found                
            
print(findJudge('self',3, [[1,2],[2,3]]))