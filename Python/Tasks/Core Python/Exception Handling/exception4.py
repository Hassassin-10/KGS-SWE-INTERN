u = "Alok"
p = "1234"

try:
    attempt = 3
    for i in range(attempt):
        user = input("Enter username: ")
        passw = input("Enter password: ")
        if user == u and passw == p:
            print("Access Granted")
    raise Exception("No more Try's")
except Exception as e:
    print("Error")