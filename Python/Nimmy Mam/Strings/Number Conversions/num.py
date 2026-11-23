s = input("Enter a String: ")

def sumDig(s):
    sumNum = 0
    astr = ""
    NewNum = ""
    for i in range(0,len(s)):
        if "0" <= s[i] <= "9":
            sumNum += (ord(s[i])-48)
        else:
            astr += s[i]
    while sumNum > 0:
        rem = sumNum % 10
        NewNum = chr(rem+48) + NewNum
        sumNum //= 10
    return astr + NewNum

res = sumDig(s)
print(res)