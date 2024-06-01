"""
برنامه ای بنویسید که به این تشخیص دهد کاربر عادی به سایت وارد شده یا ادمین؟
ادمین ها به ترتیب :
# Username | Password #
  Arshia   | 123
  Ali      | 345
"""

username = input("Enter Username : ")
password = input("Enter Password : ")

if username == "Arshia" and password == "123":
    print("Welcome Arhsia, The Admin.")
elif username == "Ali" and password == "345":
    print("Welcome Ali, The Admin.")
else:
    print("Welcome Dear", username, ".")
