n = int(input("Enter num: "))
if n % 2 == 0:
    n+=1

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(n,0,-1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()