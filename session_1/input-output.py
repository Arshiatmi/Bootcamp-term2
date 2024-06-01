# Get String Input
name = input("Enter Your Name: ")

# String Output
print("Hello " + name)

# Get Int Input
age = int(input("Enter Your Age : "))

# Multitype Output
print("Your Age Is",age)
print("Your Age Is" + age) # It Will Raise A ValueError. Because It Cant Add str To int.

# Get bool Input
is_male = bool(int(input("User Is Male Or Not? (0/1)")))

# Complex Print
print("User name Is",name,"And User Age Is",age,"And User Male Status Is",is_male)
