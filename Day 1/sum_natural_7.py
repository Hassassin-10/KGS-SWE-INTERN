num = int(input("Enter Num: "))
total = 0
series = 1
while series <= num:
    total += series
    series += 1
print("Sum is:",total)
s = (num*(num+1))/2
print("Sum to N:",int(s))