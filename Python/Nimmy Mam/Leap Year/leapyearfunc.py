def isLeap(year):
    return ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))
year = int(input("Enter year: "))
if isLeap(year):
    print(year,"is a Leap year")
else:
    print(year,"is Not s Leap year")