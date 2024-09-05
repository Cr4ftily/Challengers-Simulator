import unittest
from classes.card import Card
from classes.player import Player
import json

class TestPlayer(unittest.TestCase):

    def setUp(self):
        with open("cards_pool.json", 'r') as file:
            cards_data = json.load(file)

        self.cards_pool = [Card(**data) for data in cards_data]

        self.p1 = Player("Me")
        self.p2 = Player("Bob")

    def test_name_equality(self):
        # Test that a player is equal to their name 
        self.assertEqual("Me", self.p1)
        # Test that a player is equal to their name regardless of casing
        self.assertEqual("bob", self.p2)
        # Test that player with different names are not equal
        self.assertNotEqual(self.p1, self.p2)

    def test_different_decks(self):
        # Test that players are not referencing the same deck
        self.assertIsNot(self.p1.deck, self.p2.deck)

    def test_adding_cards(self):
        self.p1.add_card(self.cards_pool[-1])
        self.assertIn(self.cards_pool[-1], self.p1.deck)

    def test_removing_cards(self):
        self.p1.remove_card(self.cards_pool[0])
        self.p1.remove_card(self.cards_pool[0])
        self.p1.remove_card(self.cards_pool[0])
        self.assertNotIn(self.cards_pool[0], self.p1.deck)

    def test_contains(self):
        self.assertTrue(self.p1.contains(self.cards_pool[0]))
        
        self.assertFalse(self.p1.contains(self.cards_pool[-1]))
        
if __name__ == '__main__':
    unittest.main()
