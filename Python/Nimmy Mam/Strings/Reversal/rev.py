s = "sky is blue"
# res = s[::-1]
# print(res)

def rev(s):
    nstr = ""
    for i in range(0,len(s)):
        nstr = s[i] + nstr
    return nstr

res = rev(s)
print(res)