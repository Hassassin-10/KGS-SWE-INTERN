def isPrime(n):
    c = 0
    i = 1
    while i * i <= n:
        if n%i == 0:
            c += 1
            if i != (n//i):
                c += 1
        i+=1
    return c==2

n = int(input("Enter num: "))
print(isPrime(n))