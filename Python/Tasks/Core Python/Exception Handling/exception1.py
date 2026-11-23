try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")
except ValueError:
    print("Error: Value should be an integer.")