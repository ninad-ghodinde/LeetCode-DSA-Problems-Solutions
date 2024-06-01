def reverseWords(self, s):
        word=s.split()
        word.reverse()
        print(str(word))
        str2=""
        for str1 in word:
            if str1 != word[-1]:
                str2 += str1.strip() + " "
            else:
                str2 += str1.strip()
        return str2

def reverseWords2(self, s: str) -> str:
    return ' '.join(s.split()[::-1])
    
print(reverseWords("self"," s       pokEfM9Smb     CkB    "))
print(reverseWords2("self"," s       pokEfM9Smb     CkB   2 "))

print("".join("r"))