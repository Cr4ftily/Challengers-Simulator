import unittest
from classes.card import Card
from classes.player import Player
from classes.stage import Stage
import json

class TestStage(unittest.TestCase):

    def setUp(self):
        with open("cards_pool.json", 'r') as file:
            cards_data = json.load(file)

        self.cards_pool = [Card(**data) for data in cards_data]

        self.p1 = Player("Me")
        self.p2 = Player("Bob")

        self.stage = Stage(self.p1, self.p2)

    def find_player(self, name):    # given that player with name is in the player pool, return the player with that name
        for player in self.players:
            if name == player:
                return player
            
    def find_card(self, name):      # given that player with name is in the player pool, return the player with that name
        for card in self.cards_pool:
            if name == card:
                return card
            
    
            
    
            
if __name__ == '__main__':
    unittest.main()