l = [1,2,3,4,5,]
# lr = []
# for i in l:
#     lr.append(i**2)
# print(lr)

# syn: [expression for var_name in iterable if condition]
a = [i ** 2 for i in l]
print(a)

b = [i for i in range(2,10) if i%2 == 0]
print(b)