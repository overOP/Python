def wish(*names):
    for name in names:
        print(f"Hello, {name}")
wish("Pradeep", "Roshani")

def greet_all(Greeting, *namee):
    for namme in namee:
        print(Greeting, namme)
greet_all("Hi", "Pradeep", "Roshani")

def data_all(**info):
    for key, value in info.items():
        print(key,"=",value)
name = input("Enter your name: ").lower()
age = int(input("Enter your age: "))

data_all(name=name, age=age)

pi = 3.14
def area_of_circle(r):
    return pi * r * r
r = int(input("Enter the value: "))
print(area_of_circle(r))

def total(a,b):
    sum = a + b
    mins = a - b
    div = a / b
    munt = a * b
    mout = a % b
    return sum, mins, div, munt, mout

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
s,mi,d,m,mo = total(a,b)

print("total= ",s,"mines= ",mi,"div= ",d,"munt= ",m,"Mout= ",mo)