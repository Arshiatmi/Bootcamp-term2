"""
برنامه ای بنویسید که لیستی از مدیران سیستم داشته باشیم و بررسی شود که ایا نام کاربری
فرد مورد نظر در لیست مدیران است یا خیر و نسبت به ان جواب متفاوت بدهد.
"""

admins = ["Arshia","Ali","Reza"]

username = input("Enter Username: ")

# First Way
found = False
for i in admins:
    if i == username:
        found = True
        break

if found:
    print("Welcome Admin")
else:
    print("Welcome User")


# Second Way
if username in admins:
    print("Welcome Admin")
else:
    print("Welcome User")
