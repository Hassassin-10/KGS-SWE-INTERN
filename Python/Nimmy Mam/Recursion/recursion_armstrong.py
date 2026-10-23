def ASN(n,pow,asn,temp):
    if n <= 0:
        return asn == temp
    base = n % 10
    asn += (base ** pow)
    n //= 10
    return ASN(n,pow,asn,temp)
    
def count(n,c):
    if n <= 0:
        return c
    return count(n // 10,c + 1)

num = int(input("Enter num: "))
pow = count(num,0)
if ASN(num,pow,0,num):
    print(num,"is ASN")
else:
    print(num,"is not ASN")