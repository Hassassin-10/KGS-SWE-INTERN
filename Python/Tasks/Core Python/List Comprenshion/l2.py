# 2. Even Employee IDs  
# An organization has employee IDs: 
# employee_ids = [101, 102, 103, 104, 105, 106, 107, 108]
# Task: 
# Create a new list containing only the even employee IDs.

employee_ids = [101, 102, 103, 104, 105, 106, 107, 108]
ee = [i for i in employee_ids if i%2==0]
print(ee)