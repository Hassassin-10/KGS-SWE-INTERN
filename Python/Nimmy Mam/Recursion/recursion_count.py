def count(n,c):
    if n <= 0:
        return c
    return count(n // 10,c + 1)

num = int(input("Enter num: "))
if num < 0:
    num *= -1
print("Count:",count(num,0))