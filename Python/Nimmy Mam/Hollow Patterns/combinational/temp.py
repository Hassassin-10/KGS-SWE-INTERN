n = int(input("Enter num: "))
noc = n

for i in range(1,2*n):
    for k in range(n-noc):
        print(" ",end="")
    for j in range(1,noc+1):
        print(noc,end=" ")
    print()
    if i < n:
        noc -= 1
    else:
        noc += 1