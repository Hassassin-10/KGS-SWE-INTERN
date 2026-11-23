# 5. Filter High-Salary Employees  
# A company wants to identify employees earning more than 
# ₹30,000. 
# salaries = [18000, 32000, 25000, 45000, 28000, 55000, 30000] 
# Task: 
# Create a list containing salaries greater than ₹30,000. 
# Expected output: 
# [32000, 45000, 55000]

salaries = [18000, 32000, 25000, 45000, 28000, 55000, 30000]

m = [i for i in salaries if i>30000]
print(m)