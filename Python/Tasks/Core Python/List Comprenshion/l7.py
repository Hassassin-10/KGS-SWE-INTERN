# 7. Generate Login Usernames  
# A company has employee names: 
# names = ["Arun", "Priya", "Karthik", "Meena"] 
# Task: 
# Generate usernames by converting each name to lowercase and 
# adding @kgs.com. 
# Expected output: 
# ['arun@kgs.com', 'priya@kgs.com', 'karthik@kgs.com', 
# 'meena@kgs.com'] 
# Hint: 
# name.lower()

names = ["Arun", "Priya", "Karthik", "Meena"]

mail = [i.lower()+'@kgs.com' for i in names]
print(mail)