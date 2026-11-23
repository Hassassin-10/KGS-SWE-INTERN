s = "?m.5,ad!a-5m"

def charFilter(s):
    newstr = ""
    for i in range(0,len(s)):
        if "A" <= s[i] <= "Z":
            newstr += (ord(s[i])+32)
        elif ("a" <= s[i] <= "z") or ("1" <= s[i] <= "9"):
            newstr += s[i]
    return newstr

def palindrome(s):
    s = charFilter(s)
    i,j = 0,len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

res = palindrome(s)
fil = charFilter(s)
print(fil)
print(res)