def minimumLength(self, s):
    print(s)
    i=0; j=len(s)-1
    while (i<j and s[i]==s[j]):
        ch=s[i] 
        while (i<=j and s[i]==ch):
            i+=1
        while (i<=j and s[j]==ch):
            j-=1
    
    print(j-i+1)


minimumLength("self","aaabccaba")


