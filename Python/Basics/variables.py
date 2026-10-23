a = 10
b = 2 * 5
c = 5 + 5
d = 11 - 1
print(id(a)) # all are pointing to same address
print(id(b)) 
print(id(c))
print(id(d))
print(a is d) # is checks if both variables address are true or not

x=35
y=30+5
z=40-5
print(id(z))
z=10
print(id(z))

g=1,2,3
print(g)
print(type(g))

n1 = 50
n2 = n1
print(n1 is n2)

e = 1
print(id(e))
e = 2
print(id(e))
e = 3
print(id(e))