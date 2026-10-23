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
series1 = 1
series2 = 1
temp = count
print("Printing ASN's")
while count > 0:
    if ASN(series1):
        print(series1,end=" ")
        count -= 1
    series1 += 1
print("\nPrinting not ASN's")
while temp > 0:
    if not ASN(series2):
        print(series2,end=" ")
        temp -= 1
    series2 += 1