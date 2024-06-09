import unittest
from home1 import *


# This File Will Be Teached. Its For Testing In Python.

class ExersiceHomeOneTest(unittest.TestCase):
    def test_buy(self):
        target_product = get_product_by_name_or_return_none("test")
        previous_price = target_product["price"]
        previous_count = target_product["count"]
        response = buy("test",1)
        self.assertEqual(target_product["price"], previous_price + (previous_price * 0.1))
        self.assertEqual(target_product["count"], previous_count - 1)
        self.assertEqual(response, True)

        response = buy("someting_that_doesnt_exist_in_dictionary_of_products",1)
        self.assertEqual(response, False)

    def test_add(self):
        self.assertRaises(ValueError,add,"test",1,10000)

        response = add("someting_that_doesnt_exist_in_dictionary_of_products",1,10000)
        self.assertEqual(response, True)
        target_product = get_product_by_name_or_return_none("someting_that_doesnt_exist_in_dictionary_of_products")
        self.assertEqual(target_product["price"],10000)

    def test_delete(self):
        self.assertIn("test",PRODUCTS)
        response = delete("test")
        self.assertEqual(response, True)
        self.assertNotIn("test",PRODUCTS)

    def test_change(self):
        response = change("test",50,20000)
        target_product = get_product_by_name_or_return_none("test")
        self.assertEqual(target_product["price"], 20000)
        self.assertEqual(target_product["count"], 50)
        self.assertEqual(response, True)
