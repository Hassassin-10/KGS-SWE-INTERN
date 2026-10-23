def revNum(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num //= 10
    return rev

num = int(input("Enter Num: "))
print("Reverse of",num,"is :",revNum(num))