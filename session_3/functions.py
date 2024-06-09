def sum(a, b):
    return (a+b)


def minus(a, b):
    return (a-b)


def multiply(a, b):
    return (a*b)


def divide(a, b):
    return (a/b)


def print_hello():
    print("""Hello !
This Program Created For Fun :)""")


def print_hello_with_name(name):
    print("Hello " + name + " !")


def return_some_random_number():
    return 5


print_hello()
print_hello_with_name("Arshia")

print("Random Number", return_some_random_number())

print("Multiply", multiply(10, 2))
print("sum", sum(10, 2))
print("minus", minus(10, 2))
print("divide", divide(10, 2))
