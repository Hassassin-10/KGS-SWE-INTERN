class A:
    def __init__(self):
        self.A = 10
class B(A):
    def __init__(self):
        super().__init__() # parentclassname.__init__(self)
        self.B = 20
class C(B):
    def __init__(self):
        super().__init__() # super will point to its parent class
        self.C = 30

c1 = C()
print(c1.C)
print(c1.B)
print(c1.A)