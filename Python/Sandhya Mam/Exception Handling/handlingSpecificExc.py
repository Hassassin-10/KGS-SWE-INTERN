try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)
except ValueError as e:
    print("It's a ValueError")
except ZeroDivisionError as e:
    print("It's a ZDE")
except Exception as e:
    print("It's an Error")