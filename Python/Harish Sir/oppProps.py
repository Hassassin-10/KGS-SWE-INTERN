class Student:
    def __init__(self):
        self.name = "ram"
        self.usn = "1VTUCS10"
        self.qual = "BE"

    def eat(self):
        print("stud is eating")
    def study(self):
        print("stud is studying")

s1 = Student()

print(s1.name)
print(s1.qual)

s1.mob = 9831
s1.addr = "Bang"
print(s1.addr)

s1.addr = "mang"
s1.qual = "MTech"

s2 = s1
s3 = s2

print(s3.mob)
print(s2.addr)