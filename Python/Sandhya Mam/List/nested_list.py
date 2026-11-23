import copy

l = [10,20,30,[1.1,1.2],40]

print(l)
print(l[4])
print(l[3][0])
l1 = l # shallow copy
l[4] = 50
print(l1)
l2 = l.copy() # deep copy
print(l2)
l[3][1] = 100
print(l)
print(l1)
print(l2)
l3 = copy.deepcopy(l) # deep copy for nested list so that it has its own mem for nested elem
print(l3)
l[3][0] = 50
print(l)
print(l1)
print(l2)
print(l3)