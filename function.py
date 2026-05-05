# global variable
x = "awesome"
def myFunc():
    print("python is" + x)
myFunc()

# local variable
x = "awesome"
def myFunc():
    x = "pradeep"
    print("python is " + x)
myFunc()
print("python is " + x)


# use global keyword if you want to change a global variable inside a function
def myFunc():
    global x
    x = "sita"
myFunc()
print("python is" + x)


