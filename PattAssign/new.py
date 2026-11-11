n = int(input("Enter num: "))

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,n+1):
        if j == 1 or i == 1 or j == n or i == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        