def PN4(n):
    print(n)
    PN3(n-1)
    return
    print("Hello World!")

def PN3(n):
    print(n)
    PN2(n-1)
    return

def PN2(n):
    print(n)
    PN1(n-1)
    return

def PN1(n):
    print(n)
    return

num = int(input("Enter num: "))
PN4(num)