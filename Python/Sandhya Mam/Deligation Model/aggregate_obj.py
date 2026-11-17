class charger:
    def __init__(self,name):
        self.cname = name
        print("charger is ready")
    def get_charger(self):
        print("charger is ready to connect")

class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c1 = ""
        print("mobile is ready")
    def has_mobile(self,c):
        self.c1 = c
        print("both are ready to connect")

m = Mobile("Infinix")
charge = charger("nu republic")
print(m.mname)
m.has_mobile(charge)
print(m.c1.cname)
m.c1.get_charger()
del m
print(charge.cname)
charge.get_charger()