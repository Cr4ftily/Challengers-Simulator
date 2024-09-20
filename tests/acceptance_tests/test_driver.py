import unittest
from unittest.mock import patch
import io
from driver import Challengers_Simulator

class TestDriver(unittest.TestCase):
        
    def test_create(self):
        input = 'create\n'
        input += 'create user\n'
        input += 'create user me\n'
        input += 'create user john\n'
        input += 'create stage\n'
        input += 'create stage me\n'
        input += 'create stage me me\n'
        input += 'create stage bob me\n'
        input += 'create something\n'
        input += 'exit\n'
        sim = Challengers_Simulator()
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("Please provide the correct arguments. Type help add", output)
        self.assertIn("me already exists.", output)
        self.assertIn("Please provide different players to the stage", output)

        self.assertIn("john", sim.players)
        self.assertTrue("bob" == sim.stage.p1)
        self.assertTrue("me" == sim.stage.p2)

    def test_add(self):
        input = 'add\n'
        input += 'add me\n'
        input += "add me butler\n"
        input += "add tony butler\n"
        input += "add me helicopter\n"
        input += "exit\n"
        sim = Challengers_Simulator()
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("Please provide the correct arguments. Type help add", output)
        self.assertIn("tony is not a valid player name.", output)
        self.assertIn("helicopter is not a valid card name.", output)

        self.assertIn("butler", sim.players[0].deck)

    def test_remove(self):
        input = 'remove\n'
        input += 'remove me\n'
        input += "remove me talent\n"
        input += "remove alice talent\n"
        input += "remove me helicopter\n"
        input += "remove me cat\n"
        input += "exit\n"
        sim = Challengers_Simulator()
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("Please provide the correct arguments. Type help remove", output)
        self.assertIn("alice is not a valid player name.", output)
        self.assertIn("helicopter is not a valid card name.", output)
        self.assertIn("Player does not have cat", output)

        self.assertNotIn("talent", sim.players[0].deck)

    def test_reset(self):
        sim = Challengers_Simulator()
        input = "create user lark"
        input += 'reset\n'
        input += 'exit\n'
        with patch('sys.stdin', io.StringIO(input)):
            sim.cmdloop()

        self.assertNotIn("lark", sim.players)
        self.assertEqual("me", sim.stage.p1)
        self.assertEqual("bob", sim.stage.p2)

    def test_cards(self):
        sim = Challengers_Simulator()
        input = "cards\n"
        input += 'exit\n'
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("Newcomer, Make-Up Artist, Movie Star, Gangster, Cat, Clown, Vendor, Juggler, Pony, Butler, Skeleton,", output)
        self.assertIn("Spider, Rescue Pod, Shapeshifter, A.I., Cow, Jester, Stable Boy, Hermit, Pig, Merman, Sailor, Treasure,", output)
        self.assertIn("Parrot, Reporter, Talent, UFO, Band, Clones, Alien, Ghost, Teenager, Necromancer, Bat, Mime, Pyrotechnician,", output)
        self.assertIn("Clairvoyant, Rubber Duck, Cowboy, Comic Character, Director, Lion, Blacksmith, Knight, Wizard, Horse,", output)
        self.assertIn("Cook, Navigator, Lifegaurd, Shark, Mascot, Dog, Hologram, Sci-Fi Geek, Slime, Vampire, Vacuum Cleaner,", output)
        self.assertIn("Werewolf, Illusionist, Bumper Car, Teddy Bear, Heroine, T-Rex, Villian, Bard, Prince, Dragon, Siren,", output)
        self.assertIn("Kraken, Submarine, Champion, Fan-Bus", output)

    def test_player(self):
        sim = Challengers_Simulator()
        input = "player\n"
        input += "player me\n"
        input += "player smith\n"
        input += 'exit\n'
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("[Me, Bob, john]", output)
        self.assertIn("Newcomer", output)
        self.assertIn("Talent", output)
        self.assertIn("Dog", output)
        self.assertIn("Champion", output)
        self.assertIn("smith does not exist.", output)

    def test_stage(self):
        sim = Challengers_Simulator()
        input = "stage\n"
        input += 'exit\n'
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()

        self.assertIn("Me Bob", output)

    def test_battle(self):
        sim = Challengers_Simulator()
        input = "reset\n"
        input += "battle\n"
        input += "battle bob\n"
        input += "battle 10000\n"
        input += 'exit\n'
        with patch('sys.stdin', io.StringIO(input)), patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            sim.cmdloop()

        output = mock_stdout.getvalue()
        
        self.assertIn("Please provide number of times to simulate battle. Type help battle", output)
        self.assertIn("Please provide a number. Type help battle", output)
        self.assertIn("3", output[212:213])
        self.assertTrue(33 <= int(output[212:214]) <= 37)

if __name__ == '__main__':
    unittest.main()
