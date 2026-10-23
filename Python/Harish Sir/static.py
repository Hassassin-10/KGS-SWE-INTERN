class Farmer:
    r = 2.5   # static var
    def __init__(self,p1,t1):
        self.p = p1
        self.t = t1
    def disp(self):
        si = (self.p * self.t * Farmer.r)/100
        print(si)
f1 = Farmer(200000,2)
f2 = Farmer(500000,5)
f3 = Farmer(1000000,10)

f1.disp()
f2.disp()
f3.disp()