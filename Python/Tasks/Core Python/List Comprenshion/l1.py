# 1. Employee Salary Increment  
# You have a list of employee salaries: 
# salaries = [18000, 22000, 25000, 30000, 35000] 
# Task: 
# Give every employee a ₹3,000 increment using list 
# comprehension.

salaries = [18000, 22000, 25000, 30000, 35000]
inc = [i + 3000 for i in salaries]
print(inc)