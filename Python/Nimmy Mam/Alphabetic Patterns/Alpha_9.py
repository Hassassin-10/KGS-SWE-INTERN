n = int(input("Enter Num: "))

for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j < i:
            print(chr(96+j),end=" ")
        else:
            print(chr(96+i),end=" ")
    print()