def PrintNum(n):
    if n <= 0:
        return
    PrintNum(n-1)
    print(n)

num = int(input("Enter num: "))
PrintNum(num)