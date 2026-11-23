s = "sky is blue"

def rev(s,news,i):
    if i < 0:
        return news
    news = news + s[i]
    return rev(s,news,(i-1))

res = rev(s,"",len(s)-1)
print(res)