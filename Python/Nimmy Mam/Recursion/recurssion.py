def PrintNum(n):
    if n <= 0:
        return
    print(n)
    PrintNum(n-1)

num = int(input("Enter num: "))
PrintNum(num)