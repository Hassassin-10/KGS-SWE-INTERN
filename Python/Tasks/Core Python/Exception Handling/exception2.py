try:
    bal = 1000
    n = int(input("Enter the withdrawal amount:"))
    if n > bal:
        raise Exception("Error: Insufficient balance!")
    elif n <= 0:
        raise Exception("Error: withdraw amount should be greater than 0 and non negative")
    else:
        bal-=n
        print("Remaining bal:",bal)

except ValueError as e:
    print("invalid input")