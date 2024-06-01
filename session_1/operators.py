age = 18

age > 18     # False ( Greater Than )
age < 18     # False ( Smaller Than )
age == 18    # True  ( Equal )
age != 18    # False ( Not Equal )
age >= 18    # True  ( Greater Or Equal Than )
age <= 18    # True  ( Smaller Or Equal Than )

age + 10      # Returns 28 But Not Changes age.
age += 10     # Returns Nothing And Changes age to 28.
age -= 10     # Returns Nothing And Changes age to 18 Again.
age - 10      # Returns 8 But Not Changes age.

age * 10        # Returns 180 / No Variable Change
age *= 10       # Returns Nothing / Variable Set To 180
age /= 10       # Returns Nothing / Variable Set To 18.0
age / 10        # Returns 1.8 / No Variable Change
age ** 2        # Returns age Power Of 2 (18.0 * 18.0)
age **= 2       # Returns Nothing / Set age Power Of 2 (324.0)
age **= 0.5     # Returns Nothing / Set Age From 324.0 to 18.0
age = int(age)  # Set age to 18 insted of 18.0

is_male = True
print(not is_male) # Returns Nothing / Prints False

name = "Arshia"
print("Hello " + name + " !")     # Prints -> Hello Arshia !
name += " Tamimi"                 # ValueError
new_name = name + " Tamimi"       # Sets new_name To "Arshia Tamimi"
name = name + " Tamimi"           # Sets name To "Arshia Tamimi" insted of defining a new variable.


