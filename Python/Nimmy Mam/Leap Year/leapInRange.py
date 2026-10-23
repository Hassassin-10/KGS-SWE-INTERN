def isLeap(year):
    return ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))


starty = int(input("Enter start year: "))
endy = int(input("Enter end year: "))
print("Leap Years's")
if starty < endy:
    for i in range(starty,(endy+1)): # incrementing loop + 1 to end
        if isLeap(i):
            print(i)
else:
    print("Invalid i/p")