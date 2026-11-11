class Emp:
    def calculate_salary(self,Sal,HRA,DA):
        total = Sal+HRA+DA
        print("Total Salary:",total)

d = Emp()
sal = int(input("Enter basic Salary: "))
hra = int(input("Enter HRA: "))
da = int(input("Enter DA: "))
d.calculate_salary(sal,hra,da)