n = int(input("Enter n :"))
diff = 1
while n>=0:
    print(n,end=" ")
    n -= diff
    diff += 1
print("\nLast n value:",n)  