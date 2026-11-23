l = [10,20,30,40,50,60]

# if step is +v left to right , if -ve right to left
# [start:end:step] end will be n-1

print(l)
print(l[2])
print(l[2:4:+1])
# print(l[2:4:0]) look in step first 0 means Error
print(l[4:2:+1])
print(l[-2:-5:-1])
print(l[-2:1:-1])
print(l[:-2:+1])
print(l[ : :-1])
print(l[:-1:+2])

l.reverse()
print(l)