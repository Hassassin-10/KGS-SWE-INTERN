n = int(input("Enter num: "))

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(n,0,-1):
        if i == n or j == n or (i+j)==(n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()