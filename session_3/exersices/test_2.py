import unittest
from e2 import *


# This File Will Be Teached. Its For Testing In Python.

class ExersiceTwoTest(unittest.TestCase):
    def test_delta(self):
        self.assertEqual(delta(1, 2, 3), -8)
        self.assertEqual(delta(1, 3, 2), 1)
        self.assertEqual(delta(2, 4, 2), 0)

    def test_handle_delta(self):
        self.assertEqual(calculate_roots(1, 2, 3), None)
        self.assertEqual(calculate_roots(1, 3, 2), (-2, -1))
        self.assertEqual(calculate_roots(2, 4, 2), -1)
