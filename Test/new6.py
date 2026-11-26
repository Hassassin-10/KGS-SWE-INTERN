"""
Input: n = 4
Output:
*     * 
**   ** 
*** *** 
******* 
*** *** 
**   ** 
*     * 
"""

n = 4
noc = 1
nor = 1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print("*",end="")
    for k in range(abs(2*(n-i))):
        print(" ",end="")
    for k in range(1,nor+1):
        print("*",end="")
    print()
    if i < n:
        noc+=1
        nor+=1
    else:
        nor-=1
        noc-=1