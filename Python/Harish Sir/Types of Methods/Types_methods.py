class Demo:
    x = 10 # static var
    def __init__(self):
        self.y = 20
        self.z = 30
    def instanceDisp(self):
        print(self.y)
        print(self.z)
    @staticmethod
    def staticDisp():
        print(Demo.x)
    @classmethod
    def classDisp(cls):
        print("python")
d = Demo()
d.instanceDisp()
Demo.staticDisp()
Demo.classDisp()