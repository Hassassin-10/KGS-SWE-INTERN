def rec_rev(n,rev,temp):
    if n <= 0:
        return rev == temp
    digit = n % 10
    rev = (rev * 10) + digit
    n //= 10
    return rec_rev(n,rev,temp)

num = int(input("Enter num: "))
res = rec_rev(num,0,num)
print(f"Palindrome: {res}")