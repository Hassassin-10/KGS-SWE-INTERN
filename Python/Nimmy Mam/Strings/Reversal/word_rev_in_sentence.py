s = "  sky  is blue"

def word_rev(s):
    s += " "
    nwrd = ""
    nsen = ""
    i = 0
    for i in range(len(s)):
        if s[i] != " ":
            nwrd = s[i] + nwrd
        elif nwrd != "":
            if nsen == "":
                nsen += nwrd
                nwrd = ""
            else:
                nsen = nsen + " " + nwrd
                nwrd = ""
    return nsen

res = word_rev(s)
print(res)