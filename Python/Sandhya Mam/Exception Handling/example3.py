def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    finally:
        print("leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        c=10/0
        print(c)
    except Exception as e:
        print("Error in fun2")
        raise e
    finally:
        print("leaving fun2")

print("Program started")
try:
    fun1()
except Exception as e:
    print("Error in main")
finally:
    print("Program Ended")