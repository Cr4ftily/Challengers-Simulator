from classes.card import Card
from typing import List

class Player:
    trophies: int = 0
    name: str = "Anonymous"
    deck: List[Card] = [Card("Newcomer", 1,"Teal",'S'), Card("Newcomer", 1,"Teal",'S'), Card("Newcomer", 1,"Teal",'S'), 
                        Card("Talent", 2,"Teal",'S'), Card("Dog", 3,"Teal",'S'), Card("Champion", 4,"Teal",'S')]

    def add_card(self, card: Card):
        self.deck.append(card)

    def remove_card(self, card: Card):
        self.deck.remove(card)

    def contains(self, card: Card):
        if card in self.deck:
            return True
        return False

    def __init__(self, name):
        self.name = name
        self.deck = self.deck[:]

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Player):
            return self.name.lower() == other.lower()
        return self.name.lower() == other.name.lower()