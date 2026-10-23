def factor(num):
    countFact = 0
    countCycle = 0
    for i in range(1,(num+1)):
        countCycle += 1
        if num % i == 0:
            print(i,end=" ")
            countFact += 1
    return countFact , countCycle

num = int(input("Enter num: "))
countFact , countCycle = factor(num)

print(f"\nFactCount: {countFact}")
print(f"Cycles: {countCycle}")