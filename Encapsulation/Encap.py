class Employee:
    def __init__(self,name,__salary):
        self.name = name
        self.__salary = __salary

    def get_salary(self):
        print(self.__salary)

    def set_salary(self,new):
        if new < 0:
            print("Invalid Salary")
        self.__salary = new
s = Employee("Alok",200)
s.get_salary()
s.set_salary(500)
s.get_salary()
s.set_salary(-100)