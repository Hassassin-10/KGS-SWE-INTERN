def rec_rev(n,rev):
    if n <= 0:
        return rev
    digit = n % 10
    rev = (rev * 10) + digit
    n //= 10
    return rec_rev(n,rev)

num = int(input("Enter num: "))
res = rec_rev(num,0)
print(f"Reversed: {res}")