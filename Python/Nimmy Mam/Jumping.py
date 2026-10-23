while True:
    n = int(input("Enter num: "))
    if n==0:
        break
    if n==10 or n==100:
        continue                # returns control back to top and skips code below continue 
    print("Entered num is: ",n)
print("Prog Exec !!")
