n = int(input("Enter num: "))

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,n+1):
        if i == n or i == 1 or j == 1 or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()