"""
برنامه ای بنویسید که موجودی یک عطر را در دیکشنری موجودی محصولات انبار بررسی کند.
"""

perfumes = {
    "tom ford":2,
    "rovena":2,
    "savauge":0
}

user_input = input("Enter Perfume: ")

if user_input in perfumes:
    if perfumes[user_input] == 0:
        print("Mojodi 0 Hast")
    else:
        print("Be Andaze",perfumes[user_input],"Mojood Darim.")
else:
    print("Too List Nist.")
