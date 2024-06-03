"""
برنامه ای بنویسید که موجودی یک عطر را در لیست محصولات انبار بررسی کند.
"""


perfumes = ["tom ford fabiolous","rovena blue"]
user_input = input("Enter Perfume Name : ").strip().lower()

if user_input in perfumes:
    print("Ok")
else:
    print("Its Not Here.")
