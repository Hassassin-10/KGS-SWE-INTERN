def count(num):
    c = 0
    while num > 0:
        num //= 10
        c += 1
    return c

num = int(input("Enter a num: "))
res = count(num)
print("The number of digits in",num,"is",res)