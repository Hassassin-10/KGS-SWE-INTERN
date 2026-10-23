n = int(input("Enter num: "))

for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i < j:
            print(chr(96+i),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()