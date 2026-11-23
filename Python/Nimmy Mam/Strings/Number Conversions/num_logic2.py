s = input("Enter a String: ")

def sumDig(s):
    sumNum = 0
    astr = ""
    for i in range(0,len(s)):
        if "0" <= s[i] <= "9":
            sumNum += (ord(s[i])-48)
        else:
            astr += s[i]
    return astr + str(sumNum)

res = sumDig(s)
print(res)