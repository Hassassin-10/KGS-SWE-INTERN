def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
    print("leaving fun1")

def fun2():
    print("Entering fun2")
    c = 10/0  # creates mem block for storing error info and there is no try block to collect
    print(c)
    print("leaving fun2")

print("program started")
fun1()
print("program end")