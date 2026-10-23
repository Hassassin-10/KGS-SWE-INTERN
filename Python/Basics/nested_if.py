a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a > b):
    if(a > c):
        print("a is greater")

elif(b > a):
    if(b > c):
        print("b is greater")

elif(c > a):
    if(c > b): 
        print("c is greater")

else:
    print("All are same")