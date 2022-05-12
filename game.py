"""Main game object code"""
import colorama
import random

from enemies import Enemy
from utilities import clear, line, error_msg, main_map_line
from maps import starting_map, biomes, town_map, castle_map, cave_map
from pathlib import Path
from player import Player, use_inventory, use_magic, level_up_check, print_player_info
try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle


class Game:
    """Main game class"""
    def __init__(self):
        self.run = True
        self.menu = True
        self.play = False
        self.intro = True  # Plays the introduction for a new game
        self.setup = True  # True until the setup phase is complete
        self.player = None  # Initializes the player object
        self.fight = False  # Indicates a battle sequence is underway
        self.standing = True  # Avoids fight change immediately upon start of game and while using menus
        self.current_map = None
        self.starting_map = starting_map
        self.town_map = town_map
        self.castle_map = castle_map
        self.cave_map = cave_map
        self.player_type = ''
        self.x_max = 0
        self.y_max = 0

    def main_menu(self):
        """Prints menu options after the game has started"""
        clear()
        print(line)
        print("1 - Player stats")
        print("2 - Inventory")
        print("3 - Magic")
        print("4 - Save Game")
        print("5 - Load Game")
        print("6 - New Game")
        print("7 - Rules")
        print("8 - Quit Game")
        print("0 - Go Back")
        print(f"{self.player.name}'s HP: {self.player.HP}/{self.player.MAXHP}")
        print(f"{self.player.name}'s MP: {self.player.MP}/{self.player.MAXMP}")
        choice = input("< ")
        match choice:
            case "1":
                clear()
                print_player_info(self.player)
            case "2":
                self.player, _ = use_inventory(self.player)
                clear()
            case "3":
                clear()
                print(f"{self.player.name} knows these battle spells: ")
                for spell in self.player.magic:
                    if not spell.startswith('heal'):
                        print(f"\t{spell}")
                print(f"\n{self.player.name} knows these healing spells: ")
                for spell in self.player.magic:
                    if spell.startswith('heal'):
                        print(f"\t{spell}")
                self.player, _, _ = use_magic(self.player)
                clear()
            case "4":
                self.save_game()
                input("> ")
            case "5":
                print("Are you sure you want to load a game?  This will overwrite your existing game! (Y/N)")
                choice2 = input("> ")
                match choice2.split():
                    case ['Y'] | ['y']:
                        print("Loading Game")
                        self.load_game()
                    case ['N'] | ['n']:
                        self.main_menu()
                    case _:
                        input(error_msg)
            case "6":
                print("Are you sure you want to start a new game?  This will overwrite your existing game! (Y/N)")
                choice2 = input("> ")
                match choice2:
                    case 'Y' | 'y':
                        input("Press enter to load new game...")
                        self.play = False
                        self.setup = True
                    case 'N' | 'n':
                        self.main_menu()
                    case _:
                        input(error_msg)
            case "7":
                self.print_rules()
            case "8" | 'q' | 'Q':
                self.intro = False
                self.play = False
                self.run = False
            case "0":
                clear()
            case _:
                input(error_msg)
                clear()
                self.main_menu()

    def print_start_menu(self):
        """ Print main text menu prior to the game starting"""
        clear()
        print(line)
        print("1 - New Game")
        print("2 - Load Game")
        print("3 - Rules")
        print("4 - Quit Game")
        choice = input("> ")
        clear()
        match choice:
            case "1":
                self.setup = True
                self.intro = False
            case "2":
                self.load_game()
                if self.player is None:
                    input("There was an error loading the game.")
                    self.print_start_menu()
                if self.current_map == 'starting_map':
                    self.set_map(self.starting_map)
                elif self.current_map == 'town_map':
                    self.set_map(self.town_map)
                elif self.current_map == 'cave_map':
                    self.set_map(self.cave_map)
                elif self.current_map == 'castle_map':
                    self.set_map(self.castle_map)
                self.intro = False
                self.setup = False
                self.play = True
            case "3":
                self.print_rules()
            case "4":
                self.intro = False
                self.play = False
                self.run = False
            case _:
                input(error_msg)

    @staticmethod
    def print_rules():
        """Prints rules for the game"""
        clear()
        print(line)
        print("Move around the map with W (up), S (down), A (left) and d (right) keys.")
        print("Randomly encounter enemies depending on the terrain you are traversing.")
        print("Restore HP with potions and MP with ethers.")
        print("Buy items in the Item Shop and spells in the Magic Shop.")
        print(
            "Gain strength to find the key to unlock the castle.  Defeat the wizard to save the town and win!")
        print("Inventory:")
        print("Potion - Heals some HP")
        print("Mid-Potion - Heals more HP")
        print("High-Potion - Heals all HP")
        print("Ether - Restores some MP")
        print("Mid-Ether - Restores more MP")
        print("High-Ether - Restores all MP")
        input("> ")

    def save(self, save_file):
        """Actually save the data to file"""

        with open(f"saves/{save_file}.pkl", "wb") as file, \
             open(f"saves/{save_file}_starting_map.pkl", "wb") as starting_map_file, \
             open(f"saves/{save_file}_town_map.pkl", "wb") as town_map_file, \
             open(f"saves/{save_file}_cave_map.pkl", "wb") as cave_map_file, \
             open(f"saves/{save_file}_castle_map.pkl", "wb") as castle_map_file:
            pickle.dump(self.player, file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.starting_map, starting_map_file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.town_map, town_map_file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.cave_map, cave_map_file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.castle_map, castle_map_file, pickle.HIGHEST_PROTOCOL)

    def save_game(self):
        """Save game options"""

        save_file = input("Enter a name for your save file: ")
        if Path(f"{save_file}.pkl").is_file():
            choice = input(f"A save named {save_file} already exists, do you want to overwrite it? (y/n) ")
            match choice:
                case 'y':
                    self.save(save_file)
                case 'n':
                    self.save_game()
                case _:
                    print("Input not understood.")
                    self.save_game()
        else:
            self.save(save_file)
        print(f"Player data saved as {save_file}")

    def load_game(self):
        """Loads the game from a local file.  Returns loaded player data."""
        path = Path('./saves/')
        saves = []
        # Put all save files in a list
        for file in path.iterdir():
            if file.is_file() and file.name.endswith('.pkl') and not file.name.endswith('map.pkl'):
                saves.append(file.name.split('.pkl')[0])
        # If no saves available, start new game
        if len(saves) == 0:
            print("No save data found. Starting new game.")
            input("> ")
            self.create_new_player()
            self.name_player()
            clear()
            input(f"Welcome to the game, {self.player.name}!")

        # Print all save files available
        print("Available save files:")
        for index, save_file in enumerate(saves):
            print(f"\t{index + 1} - {save_file}")
        choice_ = input("Which number would you like to load? ")
        try:
            choice_ = int(choice_)
            # Load save file and return player data
            if choice_ in [x for x in range(1, len(saves) + 1)]:
                with open(f"saves/{saves[choice_ - 1]}.pkl", "rb") as save_file:
                    self.player = pickle.load(save_file)
                with open(f"saves/{saves[choice_ - 1]}_starting_map.pkl", "rb") as starting_map_file:
                    self.starting_map = pickle.load(starting_map_file)
                with open(f"saves/{saves[choice_ - 1]}_town_map.pkl", "rb") as town_map_file:
                    self.town_map = pickle.load(town_map_file)
                with open(f"saves/{saves[choice_ - 1]}_cave_map.pkl", "rb") as cave_map_file:
                    self.cave_map = pickle.load(cave_map_file)
                with open(f"saves/{saves[choice_ - 1]}_castle_map.pkl", "rb") as castle_map_file:
                    self.castle_map = pickle.load(castle_map_file)
                self.current_map = starting_map
                clear()
                print(f"Welcome back {self.player.name}!")
                input("> ")
            else:
                self.player = None
                clear()
                print("Please enter a number based on the list options.")
                input("> ")
        except ValueError:
            self.player = None
            clear()
            print("Please enter a number based on the list options.")
            input("> ")

    def set_map(self, target_map):
        """Set the current map to use and provide map boundaries
        param: target_map The map that will be loaded
        """
        self.current_map = target_map
        self.x_max = len(self.current_map) - 1
        self.y_max = len(self.current_map[0]) - 1

    def create_new_player(self):
        """Create player object"""
        self.player = None
        clear()
        choice = input("Choose a player type:\n"
                       "\t1 -Barbarian\n"
                       "\t2 -Thief\n"
                       "\t3 -Red Mage\n"
                       "\t4 -White Mage\n"
                       "\t5 -Blue Mage\n")
        match choice:
            case "1":
                self.player_type = 'barbarian'
                self.player = Player(self.player_type)
            case "2":
                self.player_type = 'thief'
                self.player = Player(self.player_type)
            case "3":
                self.player_type = 'red_mage'
                self.player = Player(self.player_type)
            case "4":
                self.player_type = 'white_mage'
                self.player = Player(self.player_type)
            case "5":
                self.player_type = 'blue_mage'
                self.player = Player(self.player_type)
            case "tester":
                self.player_type = 'tester'
                self.player = Player(self.player_type)
            case _:
                input("Input not from available options. Try again.")
                self.create_new_player()

    def name_player(self):
        """Give the player a name"""
        name = input("What is your name? ")
        clear()
        if len(name) <= 2:
            print("Name must be 3 or more characters.")
            input("> ")
            self.name_player()
        else:
            self.player.name = name

    def display_map(self):
        """Displays the explored section of the current map"""
        # Counts are needed to see if player is on that tile
        row_count = 0
        for row in range(len(self.current_map)):
            print(f"\n{main_map_line}")
            tile_count = 0
            for tile in self.current_map[row]:
                if tile['visible'] is True:
                    if (row_count, tile_count) == (self.player.x, self.player.y):
                        print(colorama.Fore.GREEN + f"{biomes[tile['type']]['display']} \033[39m",  end='')
                    else:
                        print(f"{biomes[tile['type']]['display']} ",  end='')
                else:
                    print('XXXXXXXXX| ', end='')
                tile_count += 1
            row_count += 1
        print(f"\n{main_map_line}")

    def battle(self, current_enemy):
        """Kicks of a battle sequence between the player and a randomly chosen enemy"""
        enemy = Enemy(current_enemy)
        enemy.hp = enemy.hp[0]
        enemy.maxhp = enemy.maxhp[0]
        enemy.attack = enemy.attack[0]
        while self.fight:

            while True:
                clear()
                print(f"Defeat the {enemy.name}!")
                print(line)
                print(f"{enemy.name}'s HP: {enemy.hp}/{enemy.maxhp}")
                print(f"{self.player.name}'s HP: {self.player.HP}/{self.player.MAXHP}")
                print(f"{self.player.name}'s MP: {self.player.MP}/{self.player.MAXMP}")
                print(line)
                print(f"1 - Attack")
                print(f"2 - Magic")
                print(f"3 - Inventory")
                print(line)
                action = input("> ")
                match action:
                    case "1":
                        damage = random.randint(self.player.attack - 5, self.player.attack + 5)
                        enemy.hp -= damage
                        print(f"{self.player.name} dealt {damage} damage to the {enemy.name}")
                        break
                    case "2":
                        self.player, enemy, action_taken = use_magic(self.player, self.fight, enemy)
                        clear()
                        if action_taken is True:
                            break
                    case "3":
                        self.player, action_taken = use_inventory(self.player, fight=True)
                        clear()
                        if action_taken is True:
                            break
                    case _:
                        input(error_msg)

            if enemy.hp > 0:
                print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
                self.player.HP -= enemy.attack
                if self.player.HP < 0:
                    self.player.HP = 0
                print(f"{enemy.name} dealt {enemy.attack} damage to {self.player.name}")
                print(f"{self.player.name}'s HP: {self.player.HP}/{self.player.MAXHP}")
                input("> ")
                if self.player.HP <= 0:
                    self.fight = False
                    self.play = False
                    self.run = False
                    print(line)
                    print(f"{self.player.name} was defeated.....")
                    input("GAME OVER")
                    quit()
                clear()
            else:
                print(f"You defeated the {enemy.name}!")
                self.fight = False
                print(line)
                # Award random amount of Gold between allowable values in the enemy's stats
                print(f"You've found {enemy.gold} gold!")
                self.player.gold += enemy.gold
                # Award random XP between allowable values in the enemy's stats
                print(f"You've gained {enemy.xp} XP!")
                self.player.XP += enemy.xp
                self.player = level_up_check(self.player)
                chance = random.randint(0, 100)
                if chance >= 98:
                    print(f"You've found a high potion!")
                    self.player.high_potions += 1
                elif chance >= 95:
                    print(f"You've found a mid potion!")
                    self.player.mid_potions += 1
                elif chance >= 90:
                    print(f"You've found a potion!")
                    self.player.potions += 1
                if chance <= 1:
                    print(f"You've found a high ether!")
                    self.player.high_ethers += 1
                elif chance <= 3:
                    print(f"You've found a mid ether!")
                    self.player.mid_ethers += 1
                elif chance <= 6:
                    print(f"You've found an ether!")
                    self.player.ethers += 1
                input("> ")
                clear()

    def talk_to_clayton(self):
        """Talk to the Clayton NPC. If you are worthy, maybe he'll give you a required item."""
        clear()
        if self.player.key and not self.player.won:
            input("What are you doing here?  Shouldn't you be dead or fighting the wizard?")
            input("Go on now, don't be a coward!")
        elif self.player.key and self.player.won:
            input("You did it?!?!?! I don't believe it! I can finally be free of this town!!")
            input("Clayton starts to breathe heavily and his face turns red.")
            input("You walk over to him and grab him as he collapses.")
            input("You sit helplessly beside him as Clayton dies from a heart attack.")
            input("What was this all for?")
            input("Was it all a dream?")
            input("Exhausted, you slump against the floor and fall asleep.")
            input("....")
            input(".........")
            input("..............")
            input(" THE END ")
            input("Thanks for playing my game!!!")
            exit()
        if not self.player.clayton:
            input("Hello there young man, my name is Clayton.")
            input("I've been waiting in this town for 37 years for another human!")
            input("I've been able to survive by staying in town and buying items from these shop robots.")
            input("Everything was wonderful in this town until a red robed wizard came and cast a plague upon us.")
            input("Now he just sits at the top of the castle, knowing he rules everything he can see.")
            input("The only hope I've had is that a mighty warrior would come save us.")
            self.player.clayton = True
        if not self.player.key:
            input("Clayton takes a moment to look you up and down.")
            input("...")
            input("......")
            input(".........")
            if self.player.level <= 4:
                input("It seems that I have been waiting for nothing.  You are too weak to face the wizard.")
                input("Maybe if you train harder you could someday stand a chance.")
            elif self.player.level <= 6:
                input("Hmmm....you might stand a chance against the wizard.")
                input("I'm not confident in your ability to defeat him, but what else do I have to live for.")
                input("Take this key to the tower and defeat the wizard.  Good luck to you, you'll  need it!")
                self.player.key = True
            else:
                input(f"Well now, you seem like a very strong {self.player_type}!")
                input("Finally, someone to defeat the wizard! Please take this key to the castle tower and defeat him!")
                self.player.key = True

