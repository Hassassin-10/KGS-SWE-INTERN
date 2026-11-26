from itertools import zip_longest

name = ["Alok","CJ","Tommy","Vito"]
age = [35,30,40,32]
info = list(zip(name,age))
print(info)

Nage = [27,28,26]
Ninfo = list(zip_longest(name,Nage,fillvalue="#"))
print(Ninfo)