class Fan:
    def __init__(self): # constructor,special method,init method
        self.brand = "Bajaj"
        self.color = "Black"
        self.cost = 3000
        self.noOfBlades = 3

    def on(self):
        print("Fan is on")

    def rotate(self):
        print("Fan is rotating")

f1 = Fan()

print(f1.brand)
print(f1.color)
print(f1.cost)
print(f1.noOfBlades)

f1.on()
f1.rotate()