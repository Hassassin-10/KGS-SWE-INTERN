class Radio:
    def state(self,x):
        if x == 1:
            print("Radio is on")
        else:
            print("Radio is off")

class Car:
    def __init__(self,name):
        self.cname = name
        self.r = Radio()
    def start(self):
        print("Car started")

c = Car("BMW")
c.start()
c.r.state(1)  # . goes inside mem block self stores mem address
c.r.state(0)