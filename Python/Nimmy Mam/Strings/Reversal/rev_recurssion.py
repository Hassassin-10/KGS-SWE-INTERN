s = "sky is blue"

def rev(s,nstr,i):
    if i >= len(s):
        return nstr
    nstr = s[i] + nstr
    return rev(s,nstr,(i+1))

res = rev(s,"",0)
print(res)