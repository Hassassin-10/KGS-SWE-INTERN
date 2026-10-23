n = int(input("Enter num: "))

for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i < j:
            print(chr(64+j),end=" ")
        else:
            print(chr(64+i),end=" ")
    print()