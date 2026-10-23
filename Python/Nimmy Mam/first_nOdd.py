def isEvenOdd(num):
    return num % 2 == 0

count = int(input("Enter a num: "))
series = 1
print("Printing Odd's")
while count > 0:
    if not isEvenOdd(series):
        print(series,end=" ")
        count -= 1
    series += 1