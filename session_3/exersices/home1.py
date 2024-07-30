import colorama  # pip install colorama

colorama.just_fix_windows_console()

# Do Not Change These Variables ! #
PRODUCTS = {
    "test": {
        "price": 10000,
        "count": 2
    }
}

COLORS = {
    "RED": colorama.Fore.RED,
    "GREEN": colorama.Fore.LIGHTGREEN_EX,
    "RESET": colorama.Fore.RESET,
}
# Do Not Change These Variables ! #


def get_product_by_name_or_return_none(product_name):
    global PRODUCTS
    for i, j in PRODUCTS.items():
        if i == product_name:
            return j
    return None


def colorize_text(text, color):
    return COLORS[color] + text + colorama.Fore.RESET


def print_product_list():
    print("-------------------------------------------")
    index = 1
    for i, j in PRODUCTS.items():
        print(index, ":", i, j)
        index += 1
    print("-------------------------------------------")

def print_help_text():
    print(f"""
----------------------------------------------------------------------
Hello And Welcome To My Custom Store !
You Can Use These Commands To Do Your Jobs !

{COLORS["GREEN"]}
    add         To Add New Product To Product List
    delete      To Delete Product From Product List
    change      To Change Product Count And Price From Product List
    buy         To Buy Product From Product List ( Additionally Increase The Product Price )
    list        To See Product List
    exit        Exits From App
    help        Show This Help Message
{COLORS["RESET"]}
----------------------------------------------------------------------
""")


def buy(product_name, product_count):
    global PRODUCTS
    product = get_product_by_name_or_return_none(product_name)
    if product and product["count"] >= product_count:
        product["count"] -= product_count
        product["price"] *= 1.1
        print(colorize_text("[+] Product Successfully Bought :)", "GREEN"))
        return True
    else:
        print(colorize_text("[-] There Is No Product To Buy :(", "RED"))
        return False


def add(product_name, product_count, product_price):
    global PRODUCTS
    if product_name in PRODUCTS:
        print(colorize_text(
            "[-] This Product Already Exists. Change The Product If You Want.", "GREEN"))
        return False

    PRODUCTS[product_name] = {"price": product_price, "count": product_count}
    print(colorize_text("[+] Product Successfully Added :)", "RED"))
    return True


def delete(product_name):
    global PRODUCTS

    product = get_product_by_name_or_return_none(product_name)
    if product:
        del PRODUCTS[product_name]
        print(colorize_text("[+] Product Successfully Deleted :)", "GREEN"))
        return True
    else:
        print(colorize_text(
            "[-] An Error Accured In Deleting Product.", "RED"))
        return False


def change(product_name, new_product_count, new_product_price):
    global PRODUCTS

    product = get_product_by_name_or_return_none(product_name)
    if product:
        product["price"] = new_product_price
        product["count"] = new_product_count
        print(colorize_text("[+] Product Changed :)", "GREEN"))
        return True
    else:
        print(colorize_text(
            "[-] There Is No Such Product To Change :(", "RED"))
        return False


def main():
    for i in range(10):
        cmd = input(
            "Enter Your Command (add, change, delete, buy, list, help, exit):").strip().lower()
        if cmd == "add":
            name = input("Enter Product Name : ")
            while True:
                try:
                    price = float(input("Enter Product Price : "))
                    break
                except:
                    print(colorize_text(
                        "[-] Please Enter Product Price As A Float Number :/", "RED"))
            while True:
                try:
                    count = int(input("Enter Product Count : "))
                    break
                except:
                    print(colorize_text(
                        "[-] Please Enter Product Price As An Int Number :/", "RED"))
            add(name, count, price)
        elif cmd == "delete":
            name = input("Enter Product Name : ")
            delete(name)
        elif cmd == "change":
            name = input("Enter Product Name : ")
            while True:
                try:
                    price = float(input("Enter New Product Price :"))
                    break
                except:
                    print(colorize_text(
                        "[-] Please Enter Product Price As A Float Number :/", "RED"))
            while True:
                try:
                    count = int(input("Enter New Product Count : "))
                    break
                except:
                    print(colorize_text(
                        "[-] Please Enter Product Price As An Int Number :/", "RED"))
            change(name, count, price)
        elif cmd == "buy":
            name = input("Enter Product Name : ")
            while True:
                try:
                    count = int(input("Enter New Product Count : "))
                    break
                except:
                    print(colorize_text(
                        "[-] Please Enter Product Price As An Int Number :/", "RED"))
            buy(name, count)
        elif cmd == "exit":
            break
        elif cmd == "list":
            print_product_list()
        elif cmd == "help":
            print_help_text()
        else:
            print(colorize_text("[-] There Is No Such Command :/", "RED"))


if __name__ == "__main__":
    main()
