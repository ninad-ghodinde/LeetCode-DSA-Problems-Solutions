def isPowerOfFour(self, n):
    if (n>1):
        if n%4==0 and isPowerOfFour("self", n/4):
            return True 
        else:
            return False
    elif n==1:
        return True
    else:   
        return False
    
print(isPowerOfFour("self", 8))