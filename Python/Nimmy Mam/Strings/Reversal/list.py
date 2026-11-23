s = "apples are red"

def listrev(s):
    l = list(s)
    i,j=0,len(s)-1
    while i < j:
        l[i],l[j] = l[j],l[i]
        i+=1
        j-=1
    return "".join(l)

res = listrev(s)
print(res)