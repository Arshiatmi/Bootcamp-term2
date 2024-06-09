"""
برنامه ای بنویسید که 10 دیالوگ از کاربر بگیره و به اونا جواب بده و اگه بلد نبود پیغام ندونستن رو چاپ کنه.
با استفاده از دیکشنری
"""

responses = {
    "hello":"hi",
    "bye":"bye"
}

# First Way
for i in range(10):
    data = input("Enter Prompt: ")
    found = False
    for soal,javab in responses.items():
        if data == soal:
            print(javab)
            found = True

    if not found:
        print("No Answer :(")


# Second Way
for i in range(10):
    data = input("Enter Prompt: ")
    found = False
    if data in responses:
        print(responses[data])
    else:
        print("No Answer :(")

