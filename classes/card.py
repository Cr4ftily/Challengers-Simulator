from dataclasses import field
from typing import Callable

class Card:
    name: str
    strength: int # range 1-10
    color: str # red, orange, yellow, green, teal, blue, purple
    tier: str # S, A, B, and C
    ability: Callable = field(default=lambda x: None)
    bench: bool = False
    flag_loss: bool = False
    flag_gain: bool = False
    on_attack: bool = False

    def mua(card):
        if card.strength == 1:
            return 2
        return 0
    def ms(stage):
        return None
    def gangster(stage):
        return None
    def vendor(card):
        if card.color == "yellow":
            return 1
        return 0
    def juggler(stage):
        return None
    def butler(stage):
        return None
    def skeleton():
        return 1
    def rp(bench, unique):
        bench.remove("Rescue Pod")
        if "Rescue Pod" not in bench:
            unique[0] -= 1
    def ai(card):
        if card.strength == 2:
            return 1
        return 0
    def jester(stage):
        return None
    def sb(stage):
        return None
    def hermit(stage):
        return None
    def merman(stage):
        return None
    def sailor(stage):
        return None
    def treasure():
        return 2
    def reporter(stage):
        return None
    def ufo(stage):
        return None
    def band(card):
        if card.color == "red":
            return 1
        return 0
    def ghost(stage):
        return None
    def teenager(stage):
        return None
    def necromancer(stage):
        return None
    def mime(stage):
        return None
    def clairvoyant(deck, attack, counter):  # good cards to bring up: exhuast, benchers, strength match, copies, on attack 
        for i in range(counter[0], len(deck)):
            if deck[i].strength >= attack:
                element = deck.pop(i)
                deck.insert(counter[0], element)
                return 1
        return 0
        #TODO implement better logic
    def cowboy(counter, deck, bench, unique):
        card = deck[counter[0]]
        if card not in bench:
            unique[0] += 1
        bench.append(card)
        counter[0] += 1
    def cc(cc):
        cc[0] = 2
    def director(card):
        if card.color == "green":
            return 1
        return 0
    def blacksmith(card):
        if card.color == "teal":
            return 1
        return 0
    def knight(stage):
        return None
    def wizard(stage):
        return None
    def cook(card):
        return 1
    def navigator(deck, attack, counter):
        second = False
        for i in range(counter[0], len(deck)):
            if i > counter[0] + 2:
                break
            if not second and deck[i].strength >= attack and i + 1 < len(deck) - 1:
                element = deck.pop(i+1)
                deck.insert(len(deck) - 1, element)
                return 1
            if second:
                element = deck.pop(i)
                deck.insert(counter[0], element)
                element = deck.pop(i)
                deck.insert(len(deck) - 1, element)
                return 1
            second = True
        return 0
        #TODO implement better logic
    def lifegaurd(stage):
        return None
    def mascot(stage):
        return None
    def hologram(stage):
        return None
    def vampire(stage):
        return None
    def vc(stage):
        return None
    def illusionist(unique):
        return 6 - unique[0]
    def villian(stage):
        return None
    def bard(card):
        return 1
    def prince(bench, unique):
        bench.remove("Prince")
        if "Prince" not in bench:
            unique[0] -= 1
    def siren(stage):
        return None
    def submarine(stage):
        return None
    
    ability_map = {
        "Make-Up Artist": mua,
        "Movie Star": ms,
        "Gangster": gangster,
        "Vendor": vendor,
        "Juggler": juggler,
        "Butler": butler,
        "Skeleton": skeleton,
        "Rescue Pod": rp,
        "A.I.": ai,
        "Jester": jester,
        "Stable Boy": sb,
        "Hermit": hermit,
        "Merman": merman,
        "Sailor": sailor,
        "Treasure": treasure,
        "Reporter": reporter,
        "UFO": ufo,
        "Band": band,
        "Ghost": ghost,
        "Teenager": teenager,
        "Necromancer": necromancer,
        "Mime": mime,
        "Clairvoyant": clairvoyant,
        "Cowboy": cowboy,
        "Comic Character": cc,
        "Director": director,
        "Blacksmith": blacksmith,
        "Knight": knight,
        "Wizard": wizard,
        "Cook": cook,
        "Navigator": navigator,
        "Lifegaurd": lifegaurd,
        "Mascot": mascot,
        "Hologram": hologram,
        "Vampire": vampire,
        "Vacuum Cleaner": vc,
        "Illusionist": illusionist,
        "Bumper Car": juggler,
        "Villian": villian,
        "Bard": bard,
        "Prince": prince,
        "Siren": siren,
        "Submarine": submarine
    }
    bench_map = {
        "Make-Up Artist": True,
        "Vendor": True,
        "A.I.": True,
        "Band": True,
        "Director": True,
        "Blacksmith": True,
        "Cook": True,
        "Bard": True
    }
    flag_loss_map = {
        "Rescue Pod": True,
        "Clairvoyant": True,
        "Comic Character": True,
        "Navigator": True,
        "Prince": True
    }
    flag_gain_map = {
        "Skeleton": True,
        "Treasure": True,
        "Cowboy": True,
        "Illusionist": True
    }
    on_attack_map = {
        "Movie Star": True,
        "Gangster": True,
        "Juggler": True,
        "Butler": True,
        "Sailor": True,
        "Reporter": True,
        "UFO": True,
        "Ghost": True,
        "Necromancer": True,
        "Knight": True,
        "Wizard": True,
        "Hologram": True,
        "Vampire": True,
        "Vacuum Cleaner": True,
        "Bumper Car": True,
        "Villian": True,
        "Siren": True,
        "Submarine": True
    }

    def __init__(self, name, strength = 1, color = "", tier  = "A"):
        self.name = name
        self.strength = strength
        self.color = color
        self.tier = tier
        self.ability = self.ability_map.get(name, lambda x: None)
        self.bench = self.bench_map.get(name, False)
        self.flag_loss = self.flag_loss_map.get(name, False)
        self.flag_gain = self.flag_gain_map.get(name, False)
        self.on_attack = self.on_attack_map.get(name, False)

    def continuous(self):
        return not (self.bench or self.on_attack or self.flag_gain or self.flag_loss_map)

    def __str__(self):
        # Custom string representation of the dataclass
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return self.name.lower() == other.lower()
        return self.name.lower() == other.name.lower()