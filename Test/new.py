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
    asn = 0
    power = count(n)
    while n > 0:
        base = n % 10
        asn = asn + (base ** power)
        n //= 10
    if temp < 0:
        asn *= -1
    return asn == temp

def leap(y):
    if ((y % 100 != 0)and(y % 4 == 0)) or (y % 400 == 0):
        return True

# num = int(input("Enter num: "))
# print(ASN(num))

# st = int(input("Start:"))
# en = int(input("End:"))
# if st < en:
#     print("Leap Year's")
#     for i in range(st,en+1):
#         if leap(i):
#             print(i,end=" ")
#     print("\nNon Leap Year's")
#     for i in range(st,en+1):
#         if not leap(i):
#             print(i,end=" ")

co = int(input("Enter num:"))
temp = co
series = 1
series1 = 1
while co > 0:
    if ASN(series):
        print(series,end=" ")
        co -= 1
    series += 1

print("\nNot Asn")
while temp > 0:
    if not ASN(series1):
        print(series1,end=" ")
        temp -= 1
    series1 += 1