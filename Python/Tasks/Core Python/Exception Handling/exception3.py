try:
    name = input("Enter student name: ")
    marks = int(input("Enter Marks: "))
    if not 0 <= marks <= 100:
        raise Exception("Error: Marks must be between 0 and 100.")
    else:
        print("Student Marks:",marks)
except ValueError as e:
    print("Value Error Occur")