a = 1
b = 1.2
z = "hellow"

#implicite type conversion
a += b
print("Type of the variable is", type(a))

#explicit type conversion
age = input("What is your age ?")
print(type(float(age)))

# name
name = input("what is your name? ")
print(name, type(str(name)))