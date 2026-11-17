def fib(n,n1=0,n2=1):
    if n <= 0:
        return
    print(n1,end=" ")
    fib((n-1),n2,(n1+n2))

n = int(input("Enter num: "))
fib(n)