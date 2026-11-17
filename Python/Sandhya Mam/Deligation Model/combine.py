class Car:
    def __init__(self,name):
        self.cname = name
    def get_car(self):
        print("Car is ready")

class Heart:
    def __init__(self,name):
        self.hname = name
    def get_heart(self):
        print("Heart is beating")

class Person:
    def __init__(self,name):
        self.pname = name
        self.h = Heart("H")
        self.c1 = ""
    def has_person(self,car):
        self.c1 = car
        print("Person Has Car")

p = Person("luffy")
c = Car("BMW")
print(p.pname)
print(p.h.hname)
p.h.get_heart()
p.has_person(c)
print(p.c1.cname)
p.c1.get_car()
del p
print(c.cname)
c.get_car()