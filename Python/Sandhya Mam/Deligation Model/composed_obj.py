class OS:
    def __init__(self):
        self.status = True
        print("OS is installing")
        print("OS is still installing")
    def get_os(self):
        print("OS is installed")

class Mobile:
    def __init__(self,name):
        self.mname = name
        self.o = OS()
        print("Mobile is created")
        print("With os installed")

m = Mobile("Infinix")
print(m.mname)
print(m.o.status)
m.o.get_os()
del m