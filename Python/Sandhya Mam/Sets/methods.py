s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {7,8,9,10}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
print(s1.isdisjoint(s3))
s1 = {1,2,3,4,5}
s2 = {1,2}
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s2.issubset(s2))