required_age = 4
age = input("What is your age? ")

if int(age)== required_age:
    print("You can join the school")
elif int(age) > required_age:
    print("You are late for school")
else: 
    print("You can't join the school")