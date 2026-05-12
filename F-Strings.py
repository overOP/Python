age = 24
name = "Pradeep"
txt = f"My name is {name} and I am {age} years old."
print(txt)

price = 19
txt = f"The price is {price} dollars."
print(txt)


# modifiers use of : and .2f it will show in 2 decimal place
price = 19
txt = f"The price is {price:.2f} dollars."
print(txt)

# math operations
age = 24
name = "Pradeep"
txt = f"My name is {name} and I am {age+2} years old."
print(txt)

# format() method
age = 24
name = "Pradeep"
txt = "My name is {} and I am {} years old.".format(name, age)
print(txt)
