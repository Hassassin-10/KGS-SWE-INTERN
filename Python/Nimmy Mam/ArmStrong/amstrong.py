def count(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

def ASN(n):
    temp = n
    if n < 0:
        n = n * -1
    pow = count(n)
    asn = 0
    while n > 0:
        base = n % 10
        asn = asn + (base ** pow)
        n //= 10
    if temp < 0:
        asn *= -1
    return asn == temp

n = int(input("Enter num: "))
if ASN(n):
    print(n,"is an ArmStrong Num.")
else:
    print("Not an ASN")