def sortedSquares(self, nums):
    #return sorted(x*x for x in nums)
    sqr=[]
    for i in nums:
        sqr.append(i*i)
    sqr.sort()
    return sqr

print(sortedSquares("self", [-4,-1,0,3,10])) # [0,1,9,16,100]