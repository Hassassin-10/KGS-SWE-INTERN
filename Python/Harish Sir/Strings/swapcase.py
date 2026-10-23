data = input("Enter a char: ")
newstr = ""
for i in data:
    i = ord(i)
    if i >= 65 and i <= 90:
        i += 32
        i = chr(i)
        newstr += i
    else:
        i -= 32
        i = chr(i)
        newstr += i
print(newstr)