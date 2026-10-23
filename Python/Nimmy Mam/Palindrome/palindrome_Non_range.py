def Palindrome(n):
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
sr = int(input("Enter start: "))
ed = int(input("Enter end: "))
print("Palindrome num's")
for i in range(sr,(ed+1)):
    if Palindrome(i):
        print(i,end=" ")
print("\nNot Palindrome num's")
for i in range(sr,(ed+1)):
    if not Palindrome(i):
        print(i,end=" ")