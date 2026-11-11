str = " Rama is Sleeping "

print(str.strip()) # removes space from first and last index
print(str.lstrip())
print(str.rstrip())
print(str.strip())

s = "R A M A"
s.split()
ss = ""
for i in s:
    if i == " ":
        pass
    else:
        ss = ss + i
print(ss)

st = "Rama is Sleeping"
j = st.split()
for i in range(len(j)-1,-1,-1):
    print(j[i],end=" ")
new = ""
for i in j:
    new = i + " " + new
print(new)

name = "Rama"
print("Hi {}!".format(name))
print(f"Hi {name}!")

n = input("Enter name: ")
age = input("Enter age: ")
place = input("Enter address: ")

print("name = {} \nage = {} \nplace = {}".format(n,age,place))
print(f"name = {n} \nage = {age}\nplace = {place}")

