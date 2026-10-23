def factor(num):
    for i in range(1,(num+1)):
        if num % i == 0:
            print(i,end=" ")

def countFact(num):
    c = 0
    for i in range(1,num+1):
        if num % i == 0:
            c += 1
    return c

num = int(input("Enter num: "))
factor(num)
print(f"\ncount: {countFact(num)}")