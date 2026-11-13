# Method Overloading same class same method name but diff no of parameters

class Demo:
    def disp(self,a):
        print(a)
    def disp(self,a,b):
        print(a+b)
    def disp(self,a,b,c):  # it takes last updated method
        print(a+b+c) 
d = Demo()
d.disp(10)
d.disp(10,20)
d.disp(10,20,30)