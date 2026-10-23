x = 2
y = 5
print(x,y)
x = x + y
print(x,y)

a = 5
print(a)
a += a
print(a)
b = 2
a %= b
print(a)

a="abc"
b="abc"
print(a is b)
a = []
b = []
print(a is not b)

print(True is 1)
print(True == 1)
a = 1
print(a is 1)
print(False is None)

arr = [34,34,-9,[10],"abc",24.2]
s = "abbABCsf"
val = 50

print(-9 in arr)
print("ABC" in s)
print("" in s)
print([10] in arr[3])