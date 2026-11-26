t = (10,20,30,40,50)

print(t)
t = (t[:2] + (25,) + t[2:])
print(t)
t = (t[:4] + t[5:])
print(t)