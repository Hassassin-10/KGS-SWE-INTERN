def revNum(num):
    temp = num
    if num < 0:
        num *= -1
    rev = 0
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num //= 10
    if temp < 0:
        rev *= -1
    return rev

sr = int(input("Enter start: "))
ed = int(input("Enter end: "))
print("Rev num's")
for i in range(sr,(ed+1)):
    print(revNum(i),end=" ")