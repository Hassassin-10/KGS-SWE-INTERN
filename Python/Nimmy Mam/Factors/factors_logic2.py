def factors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i,end=" ")
            if i != n//i:
                print(n//i,end=" ")
        i += 1 

def countFact(n):
    i = 1
    cf = 0
    while i * i <= n:
        if n % i ==0:
            cf += 1
            if i != n//i:
                cf += 1
        i += 1
    return cf

def countCycles(n):
    cc = 0
    i = 1
    while i * i <= n:
        cc += 1
        i+=1
    return cc

n = int(input("Enter num: "))
factors(n)
print("\nCount:",countFact(n))
print("Cycles:",countCycles(n))