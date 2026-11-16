class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    def display_student(self):
        print("Student_ID:",self.student_id)
        print("Course:",self.course)
s = Student("Hit",21,4,"Python")
s.display_person()
s.display_student()