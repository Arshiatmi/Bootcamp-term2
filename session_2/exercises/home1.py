"""
برنامه ای بنویسید که 10 دیالوگ از کاربر بگیره و به اونا جواب بده و اگه بلد نبود پیغام ندونستن رو چاپ کنه.
بدون استفاده از دیکشنری
"""


for i in range(10):
    data = input("Enter Prompt: ")
    if data == "hello":
        print("hi")
    elif data == "bye":
        print("bye")
    else:
        print("No Answer.")
