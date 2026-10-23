def count(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

def ASN(n):
    temp = n
    if n < 0:
        n *= -1
    pow = count(n)
    asn = 0
    while n > 0:
        base = n % 10
        asn = asn + (base ** pow)
        n //= 10
    if temp < 0:
        asn *= -1
    return asn == temp

sr = int(input("Enter start: "))
er = int(input("Enter end: "))
print("ASN's")
if sr > er:
    print("Invalid i/p")
else:
    for i in range(sr,(er+1)):
        if ASN(i):
            print(i,end=" ")

    print("\nNot ASN's")
    for i in range(sr,(er+1)):
        if not ASN(i):
            print(i,end=" ")