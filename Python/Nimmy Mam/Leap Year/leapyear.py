year = int(input("Enter year: "))
if((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)):
    print(year,"is Leap Year")
else:
    print("not a Leap Year")