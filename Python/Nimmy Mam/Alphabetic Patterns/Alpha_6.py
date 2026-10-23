n = int(input("Enter num: "))

c = 1
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        print(chr(96+c),end=" ")
        c+=1
        if c > 26:
            c = 1
    print()