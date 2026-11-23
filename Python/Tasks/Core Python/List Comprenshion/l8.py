# 8) 
# employees = [ 
#     ("Arun", 25000), 
#     ("Priya", 45000), 
#     ("Karthik", 28000), 
#     ("Meena", 55000), 
#     ("Rahul", 32000) 
# ] 
# Task: Create a list containing the names of employees whose 
# salary is above ₹30,000. 
# Expected output: 
# ['Priya', 'Meena', 'Rahul'] 

employees = [ 
    ("Arun", 25000), 
    ("Priya", 45000), 
    ("Karthik", 28000), 
    ("Meena", 55000), 
    ("Rahul", 32000) 
] 
ab3 = [name for name,sal in employees if sal>30000]
print(ab3)