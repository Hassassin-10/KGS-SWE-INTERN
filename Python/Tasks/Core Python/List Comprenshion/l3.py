# 3. Student Pass/Fail Status  
# You have student marks: 
# marks = [85, 42, 76, 35, 91, 28, 67] 
# Task: 
# Create a list where: 
# Marks ≥ 40 → "Pass" 
# Marks < 40 → "Fail" 
# Expected output: 
# ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail', 'Pass'] 
# Concept: List comprehension + if-else

marks = [85, 42, 76, 35, 91, 28, 67] 
res = ['Pass' if i>=40 else "Fail" for i in marks]
print(res)