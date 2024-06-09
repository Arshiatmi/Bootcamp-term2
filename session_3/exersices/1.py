"""
برنامه ای بنویسید که 4 تابع عملیات ساده ریاضی را داشته باشد و از کاربر 2 عدد و یک عملیات
ریاضی بگیرد. سپس بر اساس ورودی مورد نظر تابع مورد نظر را اجرا کند.
"""

def sum(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


number1 = int(input("Enter Number 1"))
number2 = int(input("Enter Number 2"))
operator = input("Enter Operator : ")

if operator == "+":
    print(sum(number1,number2))
elif operator == "-":
    print(minus(number1,number2))
elif operator == "*":
    print(multiply(number1,number2))
elif operator == "/":
    print(divide(number1,number2))
else:
    print("Eshtebah Zadi :/")
