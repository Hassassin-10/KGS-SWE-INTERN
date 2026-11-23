# 4. Product Price Discount  
# An e-commerce application has these product prices: 
# prices = [1000, 2500, 5000, 7500, 10000] 
# Task: 
# Apply a 10% discount to every product using list comprehension. 
# Expected output: 
# [900.0, 2250.0, 4500.0, 6750.0, 9000.0]

prices = [1000, 2500, 5000, 7500, 10000] 

dis = [i-i*0.1 for i in prices]
print(dis)