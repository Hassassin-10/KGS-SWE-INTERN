class Fan:
    def __init__(self):
        self.brand = "Havels"
        self.color = "silver"
        self.cost = 5000
        print(self.brand)
        print(self)
        print(id(self))
f1 = Fan()
print(f1)
print(id(f1))