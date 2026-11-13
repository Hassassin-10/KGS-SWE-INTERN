class A:
    def dispA(self):
        print("A")
a = A()
a.dispA()
print(A.mro())

class B:
    def dispB(self):
        print("B")
b = B()
b.dispB()
print(B.mro())

class C(A):
    def dispC(self):
        print("C")
c = C()
c.dispC()
print(C.mro())

class D(A):
    def dispD(self):
        print("D")
d = D()
d.dispD()
print(D.mro())

class E(A,B):
    def dispE(self):
        print("E")
e = E()
e.dispE()
print(E.mro())

class F(C,D):
    def dispF(self):
        print("F")
f = F()
f.dispF()
print(F.mro())

class G(D):
    def dispG(self):
        print("G")
g = G()
g.dispG()
print(G.mro())

class H(F):
    def dispH(self):
        print("H")
h = H()
h.dispH()
print(H.mro())

class I(F,G):
    def dispI(self):
        print("I")
i = I()
i.dispI()
print(I.mro())

class J(H,I):
    def dispJ(self):
        print("J")
j = J()
j.dispJ()
print(J.mro())