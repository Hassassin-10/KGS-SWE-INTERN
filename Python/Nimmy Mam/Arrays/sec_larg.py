arr = [1,9,5,3,10]
second_lar = 0
largest = 0

for i in arr:
    second_lar = largest
    if i > largest:
        largest = i
print(second_lar)
print(largest)