import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class SearchTest(unittest.TestCase):
    def test_search_by_category(self):
        discs = [DigitalVideoDisc("The Lion King", "Animation"),
                 DigitalVideoDisc("Star Wars", "Science Fiction")]
        self.assertEqual(search_by_category(discs, "animation"), [discs[0]])
        self.assertEqual(search_by_category(discs, "Drama"), [])

    def test_search_by_title(self):
        discs = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual(search_by_title(discs, "Lion"), [discs[0]])
        self.assertEqual(search_by_title(discs, "missing"), [])
        self.assertEqual(search_by_title(discs, "lion"), [discs[0]])
        self.assertEqual(search_by_title(discs, "LION"), [discs[0]])
        self.assertEqual(search_by_title([], "lion"), [])
        self.assertEqual(search_by_title(discs, ""), discs)
