l = [10,20,30,40]

print(l)
l.append(50)
print(l)
l.append(60)
print(l)
# l.append(70,80,90) # it can only take one elem
l.extend([70,80,90])
print(l)
b = [100,110,120]
l.extend(b)
print(l)
l.insert(2,25)
print(l)