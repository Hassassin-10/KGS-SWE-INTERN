def countDigit(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

def ASN(n):
    temp = n
    if n < 0:
        n *= -1
    pow = countDigit(n)
    asn = 0
    while n > 0:
        base = n % 10
        asn = asn + (base ** pow)
        n //= 10
    if temp < 0:
        asn *= -1
    return asn == temp

count = int(input("Enter a num: "))
series = 1
print("Printing ASN's")
while count > 0:
    if ASN(series):
        print(series,end=" ")
        count -= 1
    series += 1