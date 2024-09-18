from classes.card import Card
from classes.player import Player
import random
from typing import List, Callable

class Stage:
    p1: Player
    p2: Player

    p1_counter, p2_counter = [0], [0]
        
    p1_bench_list: List[Card] = []; p2_bench_list: List[Card] = []
    p1_from_bench: List[Card] = []; p2_from_bench: List[Card] = []
    p1_bench_unique, p2_bench_unique = [0], [0]
    p1_cc, p2_cc = [0], [0]

    active_player = 0
    
    attack_value = [0]
    attack_list: List[Card] = []
    
    defend_value = [0]
    defend_list: List[Card] = []

    def bench(self, bench: List[Card], card: Card):
        strength = card.strength
        for bencher in bench:                  # use bench abilities (defend)
            if bencher != "Make-Up Artist" and bencher != "Director" and bencher != "Bard":
                strength += bencher.ability(card)
        return strength

    def draw_card(self, counter, opp_counter, p: Player, opp: Player, cc, bench_list: List[Card], from_bench: List[Card], bench_unique, 
                  opponent_cc, opponent_bench_list: List[Card], opponent_from_bench: List[Card], opponent_bench_unique):
        if (counter[0] >= len(p.deck)):
            return self.active_player                   # check if current player is out of cards
        card: Card = p.deck[counter[0]]                 # get the players card
        self.attack_value[0] += card.strength + cc[0]   # update attack value
        cc[0] = 0
        for bencher in from_bench:                      # use bench abilities (attack)
            if bencher != "Cook":
                self.attack_value[0] += bencher.ability(card=card)
                
        if card.on_attack or card.continuous():         # trigger on attack or continuous ability
            match card:
                case attack if attack.on_attack:
                    attack.ability(self)
                case _:
                    card.ability(self)
        self.attack_list.append(card)                   # keep track of cards on attack

        if (self.attack_value[0] >= self.defend_value[0]):
            for defender in self.defend_list:           # check for opponent running out of bench space
                if defender not in opponent_bench_list:
                    opponent_bench_unique[0] += 1
                opponent_bench_list.append(defender)    # move defender cards to bench
                if defender.bench:                      # add bench abilities to active list
                    opponent_from_bench.append(defender)
            if len(self.defend_list) > 0 and self.defend_list[-1].flag_loss:
                top_defender = self.defend_list[-1]
                match top_defender:
                    case "Clairvoyant" |"Navigator":
                        top_defender.ability(opp.deck, self.bench(from_bench, self.attack_list[-1]), opp_counter)
                    case "Comic Character":
                        top_defender.ability(opponent_cc)  # trigger flag loss ability
                    case _:
                        top_defender.ability(opponent_bench_list, opponent_bench_unique)
            if (opponent_bench_unique[0] > 6):
                return (self.active_player + 1) % 2
            
            self.active_player = (self.active_player + 1) % 2   # update attacker to now be the defender and vice versa
            self.defend_list = self.attack_list
            self.attack_list = []
            self.attack_value[0] = 0
            self.defend_value[0] = card.strength
            for bencher in from_bench:                  # use bench abilities (defend)
                if bencher != "Make-Up Artist" and bencher != "Director" and bencher != "Bard":
                    self.defend_value[0] += bencher.ability(card)
            if card.flag_gain or card.continuous():     # trigger continuous or flag gain ability
                match card.name:
                    case "Skeleton" | "Treasure":
                       self.defend_value[0] += card.ability()
                    case "Cowboy":
                        card.ability(opp_counter, opp.deck, opponent_bench_list, opponent_bench_unique)
                    case "Illusionist":
                        self.defend_value[0] += card.ability(bench_unique)
        counter[0] += 1
        return -1

    def battle(self, number : int):
        self.reset()
        sum = 0
        count = 0
        while count < number:
            random.shuffle(self.p1.deck)
            random.shuffle(self.p2.deck)

            while True:
                if self.active_player == 0:
                    battle_over = self.draw_card(self.p1_counter, self.p2_counter, self.p1, self.p2, self.p1_cc, self.p1_bench_list, self.p1_from_bench, self.p1_bench_unique, 
                                                self.p2_cc, self.p2_bench_list, self.p2_from_bench, self.p2_bench_unique)
                    if battle_over != -1:
                        sum += battle_over
                        self.reset()
                        break
                else:
                    battle_over = self.draw_card(self.p2_counter, self.p1_counter, self.p2, self.p1, self.p2_cc, self.p2_bench_list, self.p2_from_bench, self.p2_bench_unique, 
                                                self.p1_cc, self.p1_bench_list, self.p1_from_bench, self.p1_bench_unique)
                    if battle_over != -1:
                        sum += battle_over
                        self.reset()
                        break
            count += 1
        return (100 * sum) / number
                
    def reset(self):
        self.p1_counter, self.p2_counter = [0], [0]
        
        self.p1_bench_list, self.p2_bench_list = [], []
        self.p1_from_bench, self.p2_from_bench = [], []
        self.p1_bench_unique, self.p2_bench_unique = [0], [0]
        self.p1_cc, self.p2_cc = [0], [0]

        self.active_player = 0
        
        self.attack_value = [0]
        self.attack_list = []
        
        self.defend_value = [0]
        self.defend_list = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2