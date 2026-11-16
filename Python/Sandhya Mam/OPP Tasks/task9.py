class Employee: 
    def work(self): 
        print("Employee is working") 

class Developer(Employee):
    def work(self): 
        print("Writing code")

class Tester(Employee):
    def work(self):
        print("Testing application")

class Manager(Employee):
    def work(self):
        print("Managing team")

D = Developer()
T = Tester()
M = Manager()
D.work()
T.work()
M.work()