s = "sky is blue"

def rev(s):
    news = ""
    for i in range(len(s)-1,-1,-1):
        news = news + s[i]
    return news

res = rev(s)
print(res)