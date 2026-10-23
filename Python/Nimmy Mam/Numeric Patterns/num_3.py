n = int(input("Enter a num: "))

for i in range(n, 0, -1):
    for j in range(1, 2 * n):
        if j <= n - i + 1 or j >= n + i - 1 or i == 1:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()