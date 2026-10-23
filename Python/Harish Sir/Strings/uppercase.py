data = input("Enter a char: ")
newstr = ""
for i in data:
    i = ord(i)
    if i >= 97 and i <= 122:
        i -= 32
        i = chr(i)
        newstr += i
    else:
        i = chr(i)
        newstr += i
print(newstr)