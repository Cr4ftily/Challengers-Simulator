import unittest
from classes.card import Card
import json

class TestCard(unittest.TestCase):

    def setUp(self):
        with open("cards_pool.json", 'r') as file:
            cards_data = json.load(file)

        self.cards_pool = [Card(**data) for data in cards_data]

    def test_card_equality(self):
        # Test that two cards with the same name are considered equal
        self.assertEqual(self.cards_pool[0], self.cards_pool[0])

        # Test that two cards with different attributes are not considered equal
        self.assertNotEqual(self.cards_pool[0], self.cards_pool[-1])

    def test_name_equality(self):
        # Test that a card is equal to its name
        self.assertEqual("Newcomer", self.cards_pool[0])

        # Test various upper and lower case spellings
        self.assertEqual("newComer", self.cards_pool[0])
        self.assertEqual("NEWCOMER", self.cards_pool[0])

        # Test that different names don't match card
        self.assertNotEqual("Nevvcomer", self.cards_pool[0])
        self.assertNotEqual("New comer", self.cards_pool[0])

if __name__ == '__main__':
    unittest.main()
