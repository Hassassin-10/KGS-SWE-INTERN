class Demo:
    def disp(self,*args):
        print(args)
    def disp(self,**kwargs):
        print(kwargs)
d = Demo()
d.disp(name="ai",id="jay")