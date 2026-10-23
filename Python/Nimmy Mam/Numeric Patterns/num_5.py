n = int(input("Enter num: "))

for i in range(1, 2*n):
    for j in range(1, n+1):
        if j <= i and j <= 2*n-i:
            print(j, end=" ")
    print()