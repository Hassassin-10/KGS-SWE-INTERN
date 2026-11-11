class Sol:
    def swap(self,x,y):
        temp = x
        x = y
        y = temp
        print("after")
        print(x,y)
d = Sol()
a,b = 10,20
print("before")
print(a,b)
d.swap(a,b)