from classes.card import Card
from classes.player import Player
from classes.stage import Stage
from typing import List

import json
import cmd

class IncorrectArguments(Exception):
    pass

class InvalidCard(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class InvalidPlayerName(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class InvalidCardName(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class NonExsistentPlayer(Exception):
    pass

class Challengers_Simulator(cmd.Cmd):
    intro = "Welcome to Challengers Simulator. Type help or ? to list commands.\n"
    prompt = "Challengers Simulator: "

    players: List[Player] = [Player("Me"), Player("Bob")]
    cards_pool: List[Card]
    stage: Stage = Stage(players[0], players[-1])

    def preloop(self):
        with open("cards_pool.json", 'r') as file:
            cards_data = json.load(file)

        self.cards_pool = [Card(**data) for data in cards_data]

    def find_player(self, name):    # given that player with name is in the player pool, return the player with that name
        for player in self.players:
            if name == player:
                return player
            
    def find_card(self, name):      # given that player with name is in the player pool, return the player with that name
        for card in self.cards_pool:
            if name == card:
                return card

    def do_create(self, line):
        "Create User or Stage: \ncreate user [name]\ncreate stage [user1] [user2] (replaces previous stage)\nThe first user you input will go first"
        try:
            input = line.split()
            if len(input) < 2:
                raise IncorrectArguments
            type = input[0]
            if type == "user":
                if len(input) != 2:
                    raise IncorrectArguments
                name = input[-1]
                if name in self.players:
                    raise InvalidPlayerName
                self.players.append(Player(name))
            elif type == "stage":
                if len(input) != 3:
                    raise IncorrectArguments
                p1, p2 = input[1:]
                if p1 not in self.players:
                    raise NonExsistentPlayer(p1)
                elif p2 not in self.players:
                    raise NonExsistentPlayer(p2)
                self.stage = Stage(self.find_player(p1), self.find_player(p2))
            else:
                raise Exception
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help add")
        except InvalidPlayerName:
            print("Please provice unique player name.")
        except NonExsistentPlayer:
            print(f"There is no player with the name of {NonExsistentPlayer}.")
        except Exception:
            print("Invalid promt. Type help create")

    def do_add(self, line):
        "Add a card or cards to users deck\n     add [user] [cards]\ne.g. add bob    butler cat\ntype card to see list of cards"
        try:
            input = line.split()
            if len(input) < 2:
                raise IncorrectArguments
            name = input[0]
            cards = input [1:]
            if name not in self.players:
                raise InvalidPlayerName(name)
            player = self.find_player(name)
            for card in cards:
                if card not in self.cards_pool:
                    raise InvalidCardName(card)
                player.add_card(self.find_card(card))
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help add")
        except InvalidPlayerName:
            print(f"{InvalidPlayerName} is not a valid player name.")
        except InvalidCardName:
            print(f"{InvalidCardName} is not a valid card name.")
    
    def do_remove(self, line):
        "Remove a card or cards from users deck\n     remove [user] [cards]\ne.g. remove bob    butler cat\ntype card to see list of cards"
        try:
            input = line.split()
            if len(input) < 2:
                raise IncorrectArguments
            name = input[0]
            cards = input [1:]
            if name not in self.players:
                raise InvalidPlayerName(name)
            player = self.find_player(name)
            for card in cards:
                if card not in self.cards_pool:
                    raise InvalidCardName(card)
                to_remove = self.find_card(card)
                if player.contains(to_remove):
                    player.remove_card(to_remove)
                else:
                    raise InvalidCard(card)
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help add")
        except InvalidPlayerName:
            print(f"{InvalidPlayerName} is not a valid player name.")
        except InvalidCardName:
            print(f"{InvalidCardName} is not a valid card name.")
        except InvalidCard:
            print(f"Player does not have {InvalidCard}")

    def do_player(self, line):
        "Look at list of players name or the cards of the given player\nplayer (look at list of players)\nplayer [name] (look at cards of player with given name)"
        try:
            if line == "":
                print(self.players)
            else:
                if line not in self.players:
                    raise InvalidPlayerName(line)
                player = self.find_player(line)
                print(player.deck)
        except InvalidPlayerName:
            print(f"{InvalidPlayerName} does not exist.")

    def do_stage(self, line):
        "Shows the two players on stage, where first player shown goes first."
        print(self.stage.p1, self.stage.p2)

    def do_battle(self, line):
        "Commence the battle x times on the current stage\nbattle 1\nReturns percentage of the number of times first player wins."
        print(f"{self.stage.battle(int(line))}%")

    def do_reset(self, line):
        "Clears out player list and stage; recreates default players and stage"
        self.players = [Player("Me"), Player("Bob")]
        self.stage = Stage(self.players[0], self.players[-1])
        self.do_player("")

    def do_cards(self, line):
        "Shows list of cards"
        print(self.cards_pool)

    def do_exit(self, line):
        "Exit the application"
        return True

if __name__ == '__main__':
    Challengers_Simulator().cmdloop()
