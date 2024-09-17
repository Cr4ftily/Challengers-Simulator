import unittest
from classes.card import Card
from classes.player import Player
from classes.stage import Stage
from driver import Challengers_Simulator
import json

class TestAbilities(unittest.TestCase):

    def find_player(self, name):    # given that player with name is in the player pool, return the player with that name
        for player in self.players:
            if name == player:
                return player
            
    def find_card(self, name):      # given that player with name is in the player pool, return the player with that name
        for card in self.cards_pool:
            if name == card:
                return card

    def setUp(self):
        with open("cards_pool.json", 'r') as file:
            cards_data = json.load(file)

        self.cards_pool = [Card(**data) for data in cards_data]

        self.p1 = Player("Me")
        self.p2 = Player("Bob")

        self.stage = Stage(self.p1, self.p2)
            
    def test_make_up_artist(self):  
        self.p1.deck = [self.find_card("Make-Up Artist"), self.find_card("Talent")]
        self.p2.deck = [self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Make-Up Artist"), self.find_card("Make-Up Artist")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Newcomer"), self.find_card("Newcomer")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Make-Up Artist"), self.find_card("Make-Up Artist"), self.find_card("Make-Up Artist")]
        self.p2.deck = [self.find_card("Dog"), self.find_card("Bat")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")

    def test_vendor(self):
        self.p1.deck = [self.find_card("Vendor"), self.find_card("Vendor")]
        self.p2.deck = [self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("Vendor"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Vendor"), self.find_card("Vendor"), self.find_card("Vendor")]
        self.p2.deck = [self.find_card("Dog"), self.find_card("Champion")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")

    def test_ai(self):
        self.p1.deck = [self.find_card("A.I."), self.find_card("A.I.")]
        self.p2.deck = [self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("A.I."), self.find_card("Dog")]
        self.p2.deck = [self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("A.I."), self.find_card("A.I."), self.find_card("A.I.")]
        self.p2.deck = [self.find_card("Dog"), self.find_card("Champion")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}") 
            
    def test_band(self):
        self.p1.deck = [self.find_card("Band"), self.find_card("Band")]
        self.p2.deck = [self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("Band"), self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Band"), self.find_card("Band"), self.find_card("Band")]
        self.p2.deck = [self.find_card("Bat"), self.find_card("Champion")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")

    def test_director(self):  
        self.p1.deck = [self.find_card("Director"), self.find_card("Director"), self.find_card("Champion")]
        self.p2.deck = [self.find_card("Bat"), self.find_card("Bat")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Director"), self.find_card("Director"), self.find_card("Director")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Champion"), self.find_card("Champion"), self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Director"), self.find_card("Director"), self.find_card("Director")]
        self.p2.deck = [self.find_card("Bat"), self.find_card("Fan-Bus")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")

    def test_blacksmith(self):
        self.p1.deck = [self.find_card("Blacksmith"), self.find_card("Talent")]
        self.p2.deck = [self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("Blacksmith"), self.find_card("Vendor")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")
        self.p1.deck = [self.find_card("Blacksmith"), self.find_card("Blacksmith"), self.find_card("Talent")]
        self.p2.deck = [self.find_card("Dog"), self.find_card("Dog"), self.find_card("Dog")]
        win_p = self.stage.battle(10000)
        self.assertTrue(31 <= win_p <= 35, f"{win_p}")

    def test_cook(self):  
        self.p1.deck = [self.find_card("Cook"), self.find_card("Cook"), self.find_card("Cook")]
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent"), self.find_card("Talent"), self.find_card("Dog")]
        win_p = self.stage.battle(10000)
        self.assertTrue(23 <= win_p <= 27, f"{win_p}")
        self.p2.deck = [self.find_card("Dog"), self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 0)

    def test_bard(self):  
        self.p1.deck = [self.find_card("Bard"), self.find_card("Bard")]
        self.p2.deck = [self.find_card("Bat")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("Bard"), self.find_card("Bard"), self.find_card("Bard")]
        self.p2.deck = [self.find_card("Champion"), self.find_card("Champion"), self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Bard"), self.find_card("Bard"), self.find_card("Bard")]
        self.p2.deck = [self.find_card("Bat"), self.find_card("Fan-Bus")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")

    def test_rescue_pod(self):   # TODO test if exhaust removes from unique counter when it shouldn't
        self.p1.deck = [self.find_card("Rescue Pod"), Card("A"), Card("B"), Card("C"), Card("D"), Card("E"), Card("F"), Card("G")]
        self.p2.deck = [Card("A"), Card("B"), Card("C"), Card("D"), Card("E"), Card("F"), Card("E")]
        self.assertTrue(self.stage.battle(10000) > 11)
        self.p1.add_card(self.find_card("Rescue Pod"))
        self.p1.add_card(self.find_card("Rescue Pod"))
        self.p1.add_card(Card("H"))
        self.p2.deck = [Card("A", 2), Card("B", 2), Card("C", 2), Card("D", 2), Card("E", 2)]
        win_p = self.stage.battle(10000)
        self.assertTrue(4 <= win_p <= 8, f"{win_p}")

    def test_comic_character(self):
        self.p1.deck = [self.find_card("Comic Character"), self.find_card("Comic Character")]
        self.p2.deck = [self.find_card("Fan-Bus")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Comic Character"), self.find_card("Comic Character"), self.find_card("Comic Character")]
        self.p1.deck = [self.find_card("Teddy Bear"), self.find_card("Teddy Bear")]
        self.assertTrue(self.stage.battle(100) == 100)

    def test_prince(self):   # TODO test if exhaust removes from unique counter when it shouldn't
        self.p1.deck = [self.find_card("Prince"), Card("A", 5), Card("B", 5), Card("C", 5), Card("D", 5), Card("E", 5), Card("F", 5), Card("G", 5)]
        self.p2.deck = [Card("A", 5), Card("B", 5), Card("C", 5), Card("D", 5), Card("E", 5), Card("F", 5), Card("E", 5)]
        self.assertTrue(self.stage.battle(10000) > 11)
        self.p1.add_card(self.find_card("Prince"))
        self.p1.add_card(self.find_card("Prince"))
        self.p1.add_card(Card("H", 5))
        self.p2.deck = [Card("A", 10), Card("B", 10), Card("C", 10), Card("D", 10), Card("E", 10)]
        win_p = self.stage.battle(10000)
        self.assertTrue(4 <= win_p <= 8, f"{win_p}")

    def test_clairvoyant(self): #TODO update test for better clairvoyant logic
        self.p1.deck = [self.find_card("Champion"), self.find_card("Champion"), self.find_card("Champion")]
        self.p2.deck = [self.find_card("Clairvoyant"), self.find_card("Champion"), self.find_card("Dog"), self.find_card("Newcomer")]
        win_p = self.stage.battle(10000)
        self.assertTrue(40 <= win_p <= 44, f"{win_p}")

    def test_navigator(self): #TODO update test for better navigator logic
        self.p1.deck = [self.find_card("Champion"), self.find_card("Champion"), self.find_card("Champion")]
        self.p2.deck = [self.find_card("Navigator"), self.find_card("Champion"), self.find_card("Dog"), self.find_card("Newcomer")]
        win_p = self.stage.battle(10000)
        self.assertTrue(40 <= win_p <= 44, f"{win_p}")

    def test_skeleton(self):
        self.p1.deck = [self.find_card("Skeleton"), self.find_card("Skeleton")]
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p1.deck = [self.find_card("Skeleton")]
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p2.deck = [self.find_card("Skeleton"), self.find_card("Skeleton")]
        self.p1.deck = [self.find_card("Dog"), self.find_card("Dog")]
        self.assertTrue(self.stage.battle(100) == 100)

    def test_treasure(self):
        self.p1.deck = [self.find_card("Treasure"), self.find_card("Treasure")]
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Dog"), self.find_card("Talent")]
        win_p = self.stage.battle(10000)
        self.assertTrue(48 <= win_p <= 52, f"{win_p}")
        self.p1.deck = [self.find_card("Treasure")]
        self.p2.deck = [self.find_card("Talent"), self.find_card("Talent")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p2.deck = [self.find_card("Treasure"), self.find_card("Treasure")]
        self.p1.deck = [self.find_card("Champion"), self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 100)
        
    def test_cowboy(self):
        self.p1.deck = [self.find_card("Cowboy")]
        self.p2.deck = [self.find_card("Fan-Bus")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Newcomer"), self.find_card("Newcomer"), self.find_card("Newcomer")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.add_card(self.find_card("Newcomer"))
        self.assertTrue(self.stage.battle(100) == 0)

    def test_illusionist(self):
        self.p1.deck = [self.find_card("Illusionist")]
        self.p2.deck = [self.find_card("Fan-Bus"), self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 100)
        self.p2.deck = [self.find_card("Fan-Bus"), self.find_card("Bat"), self.find_card("Champion")]
        self.assertTrue(self.stage.battle(100) == 0)
        self.p1.deck = [self.find_card("Illusionist"), Card("A"), Card("B")]
        win_p = self.stage.battle(10000)
        self.assertTrue(10 <= win_p <= 14, f"{win_p}")
        self.p2.deck = [self.find_card("Fan-Bus"), self.find_card("Bat"), self.find_card("Bat")]
        self.assertTrue(self.stage.battle(100) == 0)
        
if __name__ == '__main__':
    unittest.main()