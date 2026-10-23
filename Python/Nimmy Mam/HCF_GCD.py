def HCF(n1,n2):
    gcd = 1
    lower = n1
    if n2 < n1:
        lower = n2
    for i in range(2,(lower+1)):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print(HCF(n1,n2))