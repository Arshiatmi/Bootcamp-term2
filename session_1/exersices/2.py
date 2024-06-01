"""
برنامه ای بنویسید که سه زاویه مثلث را گرفته و بررسی کند ایا این سه زاویه میتواند سه زاویه یک مثلث باشند یا خیر.
"""

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a <= 0 or b <= 0 or c <= 0:
    print("Mosalas Nemishe :(")
    exit(0)

if a + b + c == 180:
    print("Mosalas Mishe :)")
else:
    print("Mosalas Nemishe :(")
