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

    def mua(self, stage):
        return None
    def ms(self, stage):
        return None
    def gangster(self, stage):
        return None
    def vendor(self, stage):
        return None
    def juggler(self, stage):
        return None
    def butler(self, stage):
        return None
    def skeleton(self, stage):
        return None
    def rp(self, stage):
        return None
    def ai(self, stage):
        return None
    def jester(self, stage):
        return None
    def sb(self, stage):
        return None
    def hermit(self, stage):
        return None
    def merman(self, stage):
        return None
    def sailor(self, stage):
        return None
    def treasure(self, stage):
        return None
    def reporter(self, stage):
        return None
    def ufo(self, stage):
        return None
    def band(self, stage):
        return None
    def ghost(self, stage):
        return None
    def teenager(self, stage):
        return None
    def necromancer(self, stage):
        return None
    def mime(self, stage):
        return None
    def clairvoyant(self, stage):
        return None
    def cowboy(self, stage):
        return None
    def cc(self, stage):
        return None
    def director(self, stage):
        return None
    def blacksmith(self, stage):
        return None
    def knight(self, stage):
        return None
    def wizard(self, stage):
        return None
    def cook(self, stage):
        return None
    def navigator(self, stage):
        return None
    def lifegaurd(self, stage):
        return None
    def mascot(self, stage):
        return None
    def hologram(self, stage):
        return None
    def vampire(self, stage):
        return None
    def vc(self, stage):
        return None
    def illusionist(self, stage):
        return None
    def villian(self, stage):
        return None
    def bard(self, stage):
        return None
    def prince(self, stage):
        return None
    def siren(self, stage):
        return None
    def submarine(self, stage):
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

    def __init__(self, name, strength, color, tier):
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
        return not (self.bench and self.on_attack and self.flag_gain and self.flag_loss_map and self.ability != None)

    def __str__(self):
        # Custom string representation of the dataclass
        return f"{self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return self.name.lower() == other.lower()
        return self.name.lower() == other.name.lower()