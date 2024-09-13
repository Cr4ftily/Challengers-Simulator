from classes.card import Card
from classes.player import Player
from classes.stage import Stage
from card_enums import Cards
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

class SamePlayer(Exception):
    pass

class InvalidPrompt(Exception):
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

    def enum(self, name):           # run given card name through the enums
        try:
            return Cards[name].value
        except KeyError:
            return name

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
                name = input[1]
                if name in self.players:
                    raise InvalidPlayerName(name)
                self.players.append(Player(name))
            elif type == "stage":
                if len(input) != 3:
                    raise IncorrectArguments
                p1, p2 = input[1:]
                if p1 not in self.players:
                    raise NonExsistentPlayer(p1)
                elif p2 not in self.players:
                    raise NonExsistentPlayer(p2)
                p1 = self.find_player(p1)
                p2 = self.find_player(p2)
                if p1 is p2:
                    raise SamePlayer
                self.stage = Stage(p1, p2)
            else:
                raise InvalidPrompt
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help add")
        except InvalidPlayerName as name:
            print(f"{name} already exists.")
        except NonExsistentPlayer as name:
            print(f"There is no player with the name of {name}.")
        except SamePlayer:
            print("Please provide different players to the stage")
        except InvalidPrompt:
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
                e_card = self.enum(card)
                if e_card not in self.cards_pool:
                    raise InvalidCardName(card)
                player.add_card(self.find_card(e_card))
            self.print_deck(player)
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help add")
        except InvalidPlayerName as name:
            print(f"{name} is not a valid player name.")
        except InvalidCardName as name:
            print(f"{name} is not a valid card name.")
    
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
                e_card = self.enum(card)
                if e_card not in self.cards_pool:
                    raise InvalidCardName(card)
                to_remove = self.find_card(e_card)
                if player.contains(to_remove):
                    player.remove_card(to_remove)
                else:
                    raise InvalidCard(card)
                
            self.print_deck(player)
        except IncorrectArguments:
            print("Please provide the correct arguments. Type help remove")
        except InvalidPlayerName as name:
            print(f"{name} is not a valid player name.")
        except InvalidCardName as name:
            print(f"{name} is not a valid card name.")
        except InvalidCard as card:
            print(f"Player does not have {card}")

    def do_alt(self, line):
        "Alternative card names"
        print("If cards have multiple words you can use abreviations (e.g. cc for comic character)")
        print("If a card seems to have a shorthand, try that (e.g. rex for T-rex)")
        print("Instead of typing out that full name you can use just the first 3 letters (e.g. cla for clairvoyant)")
        print("Some cards have the same first three so take note that")
        print("\tcow = cow, not cowboy\n\tclo = clown, not clones\n\tsha = shapeshifter, not shark\n\ther = hermit, not heroine\n\ttre = treasure, not T-rex")

    def print_deck(self, player):
        if not isinstance(player, Player):
            try:
                if player not in self.players:
                    raise InvalidPlayerName(player)
                player = self.find_player(player)
                print(player.deck)
            except InvalidPlayerName as name:
                print(f"{name} does not exist.")
        else:
            print(player.deck)

    def do_player(self, line):
        "Look at list of players name or the cards of the given player\nplayer (look at list of players)\nplayer [name] (look at cards of player with given name)"
        if len(line) == 0:
            print(self.players)
        else:
            self.print_deck(line)

    def do_stage(self, line):
        "Shows the two players on stage, where first player shown goes first."
        print(self.stage.p1, self.stage.p2)

    def do_battle(self, line):
        "Commence the battle x times on the current stage\nbattle 1\nReturns percentage of the number of times first player wins."
        try:
            if len(line) == 0:
                raise IncorrectArguments
            x: int
            if "\n" in line:
                x = int(line.replace('\n', ''))
            x = int(line)
            win_p = self.stage.battle(x)
            print(f"{win_p}%")
        except IncorrectArguments:
            print("Please provide number of times to simulate battle. Type help battle")
        # except Exception:
        #     print("Please provide a number. Type help battle")

    def do_reset(self, line):
        "Clears out player list and stage; recreates default players and stage"
        self.players = [Player("Me"), Player("Bob")]
        self.stage = Stage(self.players[0], self.players[-1])
        self.do_player("")

    def do_cards(self, line):
        "Shows list of cards"
        cards = ""
        for card in self.cards_pool:
            cards += card.name + ", "
            if len(cards) > 100:
                print(cards)
                cards = ""
        print(cards[:-2])

    def do_exit(self, line):
        "Exit the application"
        return True

if __name__ == '__main__':
    Challengers_Simulator().cmdloop()
