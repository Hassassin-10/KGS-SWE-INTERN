class Demo:
    def __init__(self):
        self.a = 10   # instance variable
        self.b = 20
    def disp(self,x,y):
        z = x + y
        return z
d1 = Demo()
print(d1.a)
print(d1.b)
n1 = 100    # local variable
n2 = 200
r = d1.disp(n1,n2)
print(r)