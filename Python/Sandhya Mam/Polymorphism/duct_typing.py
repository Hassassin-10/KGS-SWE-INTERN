class Plane:
    def takeoff(self):
        print("Plane is takeoff")
    def land(self):
        print("Plane is landing")

class Cargo:
    def takeoff(self):
        print("Cargo is takeoff")
    def land(self):
        print("Cargo is landing")

class Passenger:
    def takeoff(self):
        print("Passenger is takeoff")
    def land(self):
        print("Passenger is landing")

class Fighter:
    def takeoff(self):
        print("Fighter is takeoff")
    def land(self):
        print("Fighter is landing")
        
pl = Plane()
c = Cargo()
p = Passenger()
f = Fighter()

def allowPlane(ref):
    ref.takeoff()
    ref.land()

allowPlane(pl)
allowPlane(c)
allowPlane(p)
allowPlane(f)