
def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    #final=candies.copy()
    boolist=[]
    #print(final)
    #final.sort(reverse=True)
    #highest=final[0]
    #print(candies)
    for i in candies:
        if(i+extraCandies >= max(candies)):
            boolist.append(True)
        else:
            boolist.append(False)
    return boolist
    

print(kidsWithCandies("self",[2,3,5,1,3],3))
