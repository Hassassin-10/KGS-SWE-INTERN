a = int(input("Enter a num1: "))
b = int(input("Enter a num2: "))
try:
    c = a/b
    print(c)
except Exception as e:
    print("Error is occurred")