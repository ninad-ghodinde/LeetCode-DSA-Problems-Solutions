def findMaxLength(self, nums):
    cnt1=sum (1 for x in nums if x==1)
    cnt0=sum (1 for x in nums if x==0)  
    if cnt1==cnt0:
        return(cnt1*2)
    elif cnt1>cnt0:
        return(cnt0*2)
    else:
        return(cnt1*2)

print(findMaxLength("self",[1,0,1   ]))