n = int(input("Enter num: "))

for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(chr(96+j),end=" ")
    print()