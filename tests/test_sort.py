import contextlib
import io
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            self.cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
            self.cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
            self.cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([dvd.title for dvd in self.cart.items],
                         ["Aladdin", "Star Wars", "The Lion King"])
        self.assertAlmostEqual(self.cart.total_cost(), 63.89)

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([dvd.cost for dvd in self.cart.items], [18.99, 19.95, 24.95])
        self.assertAlmostEqual(self.cart.total_cost(), 63.89)
