def minWindow(self, s, t):
    if len(s)==len(t) and s==t:
        return s
    if len(s)<len(t):
        if t != s:
            return ""
    contains=[]
    for i in range(0,len(s)):
        str=""
        for j in range(i,len(s)):
            str=str+s[j]
            checker=0
            for k in t:
                if k in str:
                    checker+=1
            if checker>=len(t):
                contains.append(str)
            continue

    print(contains)
    contains.sort(key=len)
    print(contains)
    if len(contains) == 0:
        return ""
    else:   
        i=0
        flag=True
        while flag:
            string1=''.join(str for str in contains[i])
            if (check_characters(string1,t))==1:
                flag=False
            else:
                i+=1
            #print(i,contains[i])
        return ''.join(str for str in contains[i])

def check_characters(string1, string2):
    for char in string2:
        if char not in string1:            
            return 0
        else:
            string1 = string1.replace(char, '', 1)
    return 1

print(minWindow("self","ADOBECODEBANC", "ABC"))    
print(minWindow("self","abc", "ab"))   
print(minWindow("self","bbaa", "aba")) 
print(minWindow("self","ab", "a"))
