# s = {10,20,{70,5},6} # set inside a set not allowed
# print(s)
# s = {10,20,[70,5],6} # list inside a set not allowed 
# print(s)
s = {10,20,6,(70,5,5),6} # tuple inside a set is allowed
print(s)
s.remove((70,5,5))
print(s)