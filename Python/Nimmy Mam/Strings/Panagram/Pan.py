s = "The five boxing wizards jump quickly"
s1 = "Pack my box with five dozen liquor jugs"
a = "Vito will come to my Home now we will go to Play GTA 6"

def filter(s):
    res = ""
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            res += chr(ord(s[i])+32)
        elif "a" <= s[i] <= "z":
            res += s[i]
    return res

def Pangram(s):
    s = filter(s)
    if len(s) < 26:
        return False
    else:
        alpha = [0]*26
        for i in range(0,len(s)):
            alpha[ord(s[i])-97] = alpha[ord(s[i])-97] + 1
        print(alpha)
        for i in alpha:
            if i == 0:
                return False
    return True

res = Pangram(s1)
print(res)