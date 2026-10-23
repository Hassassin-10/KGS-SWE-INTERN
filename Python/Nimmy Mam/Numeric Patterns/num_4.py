""" 
4 3 2 1
  3 2 1
    2 1
      1
    2 1
  3 2 1
4 3 2 1 
"""

n = int(input("Enter num: "))

for i in range(1,n*2):
    for j in range(n,0,-1):
        if j <= abs(i-n)+1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()