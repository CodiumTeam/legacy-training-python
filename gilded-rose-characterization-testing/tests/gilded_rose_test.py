import unittest
from gilded_rose import GildedRose, Item

class TestGildedRose(unittest.TestCase):

    def test_xxx(self):
        items = [Item("Book", 10, 5)]
        app = GildedRose(items)

        app.update_quality()

        self.assertEqual("Book", app.items[0].name)