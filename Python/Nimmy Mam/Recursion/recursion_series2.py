def rec(n,i):
    if i > n:
        return
    print(i,end=" ")
    rec(n,i+1)
    print(i,end=" ")

num = int(input("Enter num: "))
rec(num,1)  