def rev(n):
    temp = n
    if n < 0:
        n *= -1
    rev = 0
    while n > 0:
        dig = n % 10
        rev = (rev * 10) + dig
        n //= 10
    if temp < 0:
        rev *= -1
    return rev

n = int(input("Enter num: "))
print("Reverse is:",rev(n))