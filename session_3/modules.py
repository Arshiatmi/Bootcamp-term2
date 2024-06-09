import random

print(random.randint(0,10))   # Pick A Random Number Between 0 And 10
print(random.randint(10,100)) # Pick A Random Number Between 10 And 100



import pyfiglet # Install Package With 'pip install pyfiglet'

result = pyfiglet.figlet_format("Hello There :)", font = "slant")
print(result)
