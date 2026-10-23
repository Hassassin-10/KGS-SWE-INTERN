def Palindrome(num):
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
    return rev == temp

n = int(input("Enter num: "))
count = 0
series = 1

while count < n:
    if Palindrome(series):
        print(series, end=" ")
        count += 1
    series += 1