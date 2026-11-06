import contextlib
import io
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            self.cart.add_dvd(DigitalVideoDisc("DVD", cost=100))

    def test_discounted_total(self):
        self.assertEqual(self.cart.total_cost_with_discount(20), 80)
        self.assertEqual(self.cart.total_cost_with_discount(0), 100)
        self.assertEqual(self.cart.total_cost_with_discount(100), 0)

    def test_invalid_discount(self):
        for percent in (-1, 150):
            with self.subTest(percent=percent), self.assertRaises(ValueError):
                self.cart.total_cost_with_discount(percent)
