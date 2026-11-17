def palindrome(n):
    temp = n
    if n < 0:
        n *= -1
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n //= 10
    if temp < 0:
        rev *= -1
    return rev == temp

count = int(input("Enter num: "))
series = 1
while count > 0:
    if palindrome(series):
        print(series,end=" ")
        count -= 1
    series += 1