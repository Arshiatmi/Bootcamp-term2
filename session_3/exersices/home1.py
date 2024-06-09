# Do Not Change This Variable ! #
PRODUCTS = [
    {
        "name": "test",
        "price": 10000,
        "count": 2
    }
]
# Do Not Change This Variable ! #

def get_product_by_name_or_return_none(product_name):
    global PRODUCTS
    for i in PRODUCTS:
        if i["name"] == product_name:
            return i
    return None


def buy(product_name, product_count):
    global PRODUCTS
    pass


def add(product_name, product_count, product_price):
    global PRODUCTS
    pass


def delete(product_name):
    global PRODUCTS

    if product_name in PRODUCTS:
        del PRODUCTS[product_name]
        return True
    else:
        return False


def change(product_name, new_product_count, new_product_price):
    global PRODUCTS
    pass


def main():
    # Write Your Codes Here :)
    pass

if __name__ == "__main__":
    main()
