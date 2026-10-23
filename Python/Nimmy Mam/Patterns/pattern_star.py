print("*")
print("-------")

num = int(input("Enter Num:")) # multiple rows & single col
for i in range(1,num+1):
    print("*")
print("-------")

for j in range(1,num+1): # one row multiple cols
    print("*",end=" ")
print("\n-------")

for j in range(num,(1-1),-1):
    print("*",end=" ")
print("\n-------")

