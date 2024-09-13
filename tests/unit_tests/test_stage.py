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
            
    def test_battle(self):
        win_p =  self.stage.battle(10000)
        self.assertTrue(33 <= win_p <= 37, f"{win_p}")

    def test_reset(self):
        stage = self.stage
        stage.battle(1)
        self.assertEqual(stage.active_player, 0)
        self.assertEqual(stage.attack_list, [])
        self.assertEqual(stage.attack_value, [0])
        self.assertEqual(stage.defend_list, [])
        self.assertEqual(stage.defend_value, [0])
        self.assertEqual(stage.p1_bench_list, [])
        self.assertEqual(stage.p1_bench_unique, [0])
        self.assertEqual(stage.p1_cc, [0])
        self.assertEqual(stage.p1_counter, [0])
        self.assertEqual(stage.p1_from_bench, [])
        self.assertEqual(stage.p2_bench_list, [])
        self.assertEqual(stage.p2_bench_unique, [0])
        self.assertEqual(stage.p2_cc, [0])
        self.assertEqual(stage.p2_counter, [0])
        self.assertEqual(stage.p2_from_bench, [])
    
            
    
            
if __name__ == '__main__':
    unittest.main()