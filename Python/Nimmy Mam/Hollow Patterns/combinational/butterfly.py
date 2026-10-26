n = int(input("Enter num: "))

for i in range(1,n*2):
    for j in range(1,n*2):
        if j == 1 or j == ((n*2)-1) or i == j or (i+j) == (n*2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()