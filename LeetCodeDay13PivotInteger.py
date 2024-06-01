def pivotInteger(self, n):
    sum=int((n*(n+1))/2)
    print("sum",sum)    
    sumrun=0
    for i in range(1,n+1):
        sumrun+=i
        print("sumrun",sumrun)
        if (sum-(sumrun))==sumrun-i:
            return i
    return -1
        

    

print(pivotInteger("self", 4))
print(pivotInteger("self", 8))