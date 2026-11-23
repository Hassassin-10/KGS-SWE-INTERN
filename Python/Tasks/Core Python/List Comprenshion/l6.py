# 6. Convert Names to Uppercase  
# An HR system stores employee names: 
# employees = ["arun", "priya", "karthik", "meena", "rahul"] 
# Task: 
# Convert all employee names to uppercase using list 
# comprehension. 
# Expected output: 
# ['ARUN', 'PRIYA', 'KARTHIK', 'MEENA', 'RAHUL'] 
# Concept: List comprehension + string methods

employees = ["arun", "priya", "karthik", "meena", "rahul"] 

op = [i.upper() for i in employees]
print(op)