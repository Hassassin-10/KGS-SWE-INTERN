class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def land(self):
        print("Plane is landing")

class Cargo(Plane):
    def takeoff(self):
        print("Cargo is takeoff")
    def land(self):
        print("Cargo is landing")

class Passenger(Plane):
    def takeoff(self):
        print("Passenger is takeoff")
    def land(self):
        print("Passenger is landing")

class Fighter(Plane):
    def takeoff(self):
        print("Fighter is takeoff")
    def land(self):
        print("Fighter is landing")

c = Cargo()
p = Passenger()
f = Fighter()

def allowPlane(ref):
    ref.takeoff()
    ref.land()

allowPlane(c)
allowPlane(p)
allowPlane(f)