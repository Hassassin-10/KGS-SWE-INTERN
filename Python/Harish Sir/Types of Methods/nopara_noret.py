class Demo:
    def __init__(self):
        self.a = 10   # instance variable
        self.b = 20
    def disp(self):
        x = 100       # local variable
        y = 200
        z = x + y
        print(z)
d1 = Demo()
print(d1.a)
print(d1.b)
d1.disp()