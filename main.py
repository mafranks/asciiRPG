"""Main file for the ASCII RPG"""
import os
import random
import time

from enemies import Enemy, enemy_list
from maps import starting_map, biomes, town_map
from player import Player, use_inventory, print_player_info, use_magic, level_up_check
from shops import item_shop, magic_shop, inn
from utilities import clear, error_msg

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle


run = True
menu = True
play = False
intro = True  # Plays the introduction for a new game
setup = True  # True until the setup phase is complete
player = None  # Initializes the player object
fight = False  # Indicates a battle sequence is underway
standing = True  # Avoids fight change immediately upon start of game

# TODO - Add variable save name so multiple saves can exist
save_file = "save_file.pkl"
line = "--------------------"


def set_map(target_map):
    # Set the current map to use and provide map boundaries
    current_map = target_map
    x_max = len(current_map) - 1
    y_max = len(current_map[0]) - 1
    return current_map, x_max, y_max

def print_start_menu():
    """ Print main text menu prior to the game starting"""
    clear()
    print(line)
    print("1 - New Game")
    print("2 - Load Game")
    print("3 - Rules")
    print("4 - Quit Game")


def print_rules():
    """Prints rules for the game"""
    clear()
    print(line)
    print("Move around the map with W (up), S (down), A (left) and d (right) keys.")
    print("Randomly encounter enemies depending on the terrain you are traversing.")
    print("Restore HP with potions and MP with ethers.")
    print("Buy items in the Item Shop and spells in the Magic Shop.")
    print("Gain strength to find the key to unlock the castle.  Defeat the dragon to save the Royal Family and win!")
    print("Inventory:")
    print("Potion - Heals 10 HP")
    print("Mid-Potion - Heals 25 HP")
    print("High-Potion - Heals 50 HP")
    print("Ether - Heals 2 MP")
    print("Mid-Ether - Heals 5 MP")
    print("High-Ether - Heals 10 MP")
    input("> ")


def create_new_player():
    """Create player object"""
    clear()
    player = Player()

    def name_player():
        """Give the player a name"""
        name = input("What is your name? ")
        clear()
        if len(name) <= 2:
            print("Name must be 3 or more characters.")
            input("> ")
            name_player()
        else:
            player.name = name
    name_player()
    print(f"Welcome to the game, {player.name}!")
    # TODO - Add choice for player type
    # TODO - Add different player attributes to choose from
    return player


def main_menu(player_data):
    """Prints menu options after the game has started"""
    global intro, play, run, setup
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
    print(f"{player_data.name}'s HP: {player_data.HP}/{player_data.MAXHP}")
    print(f"{player_data.name}'s MP: {player_data.MP}/{player_data.MAXMP}")
    choice = input("< ")
    match choice.split():
        case ["1"]:
            clear()
            player_data = print_player_info(player_data)
        case ["2"]:
            player_data, _ = use_inventory(player_data)
            clear()
        case ["3"]:
            print(f"{player.name} knows these battle spells: ")
            for spell in player.magic:
                if not spell.startswith('heal'):
                    print(spell)
            heals = [spell for spell in player.magic if spell.startswith('heal')]
            if len(heals) == 0:
                print(f"{player.name} doesn't know any healing spells. Visit the Magic Shop.")
            else:
                print(f"{player.name} knows these healing spells: ")
                for spell in player.magic:
                    if spell.startswith('heal'):
                        print(spell)
            player_data, _, _ = use_magic(player_data)
            clear()
        case ["4"]:
            save(player_data)
            input("> ")
        case ["5"] | ["Load"] | ["Load", "Game"]:
            print("Are you sure you want to load a game?  This will overwrite your existing game! (Y/N)")
            choice2 = input("> ")
            match choice2.split():
                case ['Y'] | ['y']:
                    print("Loading Game")
                    player_data = load()
                case ['N'] | ['n']:
                    main_menu(player_data)
                case _:
                    input(error_msg)
        case ["6"] | ['New'] | ['New', 'Game']:
            print("Are you sure you want to start a new game?  This will overwrite your existing game! (Y/N)")
            choice2 = input("> ")
            match choice2.split():
                case ['Y'] | ['y']:
                    print("Loading New Game")
                    player_data = create_new_player()
                case ['N'] | ['n']:
                    main_menu(player_data)
                case _:
                    input(error_msg)
        case ["7"] | ['Rules']:
            print_rules()
        case ["8"] | ['Quit'] | ['Quit', 'Game'] | ['q'] | ['Q']:
            intro = False
            play = False
            run = False
        case _:
            input(error_msg)
            clear()
            main_menu(player_data)

    return player_data


def save(player_data):
    """Save the game to a local file"""
    # TODO - Save map data with the player
    # Set player to start of the map for consistency
    player.x = 0
    player.y = 0
    with open(save_file, "wb") as file:
        pickle.dump(player_data, file, pickle.HIGHEST_PROTOCOL)
    print("Player data saved")
    # TODO - Add unique save names so multiple saves are available


def load():
    """Loads the game from a local file"""
    if os.path.exists(save_file):
        with open(save_file, "rb") as file:
            player_data = pickle.load(file)
            print(f"Welcome back {player_data.name}!")
            return player_data
    else:
        print("No save file found.")
    # TODO - Add print for each save file and option to choose which one to load


def display_map(current_map):
    """Displays the explored section of the current map"""
    for row in range(len(current_map)):
        print(f"\n{line * (x_max - 1)}----------------")
        for tile in current_map[row]:
            if tile['visible'] is True:
                print(f"{biomes[tile['type']]['display']} ",  end='')
            else:
                print('XXXXXXXXX| ', end='')
    print(f"\n{line * (x_max - 1)}----------------")


def battle(current_enemy, player_data):
    """Kicks of a battle sequence between the player and a randomly chosen enemy"""
    global fight, play, run, line
    enemy = Enemy(current_enemy)
    # TODO - Figure out why hp and maxhp convert to tuples ?!?!
    enemy.hp = enemy.hp[0]
    enemy.maxhp = enemy.maxhp[0]
    enemy.attack = enemy.attack[0]
    while fight:

        while True:
            clear()
            print(f"Defeat the {enemy.name}!")
            print(line)
            print(f"{enemy.name}'s HP: {enemy.hp}/{enemy.maxhp}")
            print(f"{player_data.name}'s HP: {player_data.HP}/{player_data.MAXHP}")
            print(f"{player_data.name}'s MP: {player_data.MP}/{player_data.MAXMP}")
            print(line)
            print(f"1 - Attack")
            print(f"2 - Magic")
            print(f"3 - Inventory")
            print(line)
            action = input("> ")
            match action.split():
                case ["1"] | ["Attack"]:
                    # TODO - Make attack a range based on attack strength
                    enemy.hp -= player_data.attack
                    print(f"{player_data.name} dealt {player_data.attack} damage to the {enemy.name}")
                    break
                case ["2"] | ["Magic"]:
                    player, enemy, action_taken = use_magic(player_data, fight, enemy)
                    clear()
                    if action_taken is True:
                        break
                case ["3"] | ["Inventory"]:
                    player_data, action_taken = use_inventory(player_data)
                    clear()
                    if action_taken is True:
                        break
                case _:
                    input(error_msg)

        if enemy.hp > 0:
            print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
            player_data.HP -= enemy.attack
            if player_data.HP < 0:
                player_data.HP = 0
            print(f"{enemy.name} dealt {enemy.attack} damage to {player_data.name}")
            print(f"{player_data.name}'s HP: {player_data.HP}/{player_data.MAXHP}")
            input("> ")
            if player_data.HP <= 0:
                fight = False
                play = False
                run = False
                print(line)
                print(f"{player_data.name} was defeated.....")
                input("GAME OVER")
                quit()
            clear()
        else:
            print(f"You defeated the {enemy.name}!")
            fight = False
            print(line)
            # Award random amount of Gold between allowable values in the enemy's stats
            print(f"You've found {enemy.gold} gold!")
            player_data.gold += enemy.gold
            # Award random XP between allowable values in the enemy's stats
            print(f"You've gained {enemy.xp} XP!")
            player_data.XP += enemy.xp
            player_data = level_up_check(player_data)
            chance = random.randint(0, 100)
            if chance >= 98:
                print(f"You've found a high potion!")
                player_data.high_potions += 1
            elif chance >= 95:
                print(f"You've found a mid potion!")
                player_data.mid_potions += 1
            elif chance >= 90:
                print(f"You've found a potion!")
                player_data.potions += 1
            if chance <= 1:
                print(f"You've found a high ether!")
                player_data.high_ethers += 1
            elif chance <= 3:
                print(f"You've found a mid ether!")
                player_data.mid_ethers += 1
            elif chance <= 6:
                print(f"You've found an ether!")
                player_data.ethers += 1
            input("> ")
            clear()

    return player_data


while run:
    while intro:
        clear()
        print_start_menu()
        choice = input("> ")
        clear()
        match choice.split():
            case ["1"] | ['New'] | ['New', 'Game']:
                setup = True
                intro = False
            case ["2"] | ['Load'] | ['Load', 'Game']:
                player = load()
                current_map, x_max, y_max = set_map(starting_map)
                intro = False
                setup = False
                play = True
            case ["3"] | ['Rules']:
                print_rules()
            case ["4"] | ['Quit'] | ['Quit', 'Game']:
                intro = False
                play = False
                run = False
            case _:
                input(error_msg)

    while setup:
        clear()
        player = create_new_player()
        current_map, x_max, y_max = set_map(starting_map)
        input("> ")
        play = True
        setup = False

    while play:
        clear()
        current_tile = current_map[player.x][player.y]['type']
        current_map[player.x][player.y]['visible'] = True
        if not standing and biomes[current_tile]['enemies'] and random.randint(0, 100) < 25:
            fight = True
            enemy = enemy_list[random.randrange(0, len(enemy_list))]
            player = battle(enemy, player)

        display_map(current_map)
        print(f"LOCATION: {biomes[current_tile]['text']} {player.x, player.y}")
        print(f"Move with W,S,A,D")
        print(f"0 to view menu")
        if current_tile == 'item_shop':
            print(f"1 to visit the Item Shop")
        elif current_tile == 'magic_shop':
            print(f"2 to visit the Magic Shop")
        elif current_tile == 'town':
            print(f"3 to visit the Town")
        elif current_tile == 'inn':
            print(f"4 to visit the Inn")
        elif current_tile == 'entrance':
            print(f"9 to return to map")
        # TODO - Make player position more obvious in the map
        destination = input("> ")
        match destination.split():
            case ["0"]:
                player = main_menu(player)
            case ["W"] | ["w"]:
                standing = False
                if player.x > 0:
                    player.x -= 1
                else:
                    player.x = x_max
            case ["S"] | ["s"]:
                standing = False
                if player.x < x_max:
                    player.x += 1
                else:
                    player.x = 0
            case ["A"] | ["a"]:
                standing = False
                if player.y > 0:
                    player.y -= 1
                else:
                    player.y = y_max
            case ["D"] | ["d"]:
                standing = False
                if player.y < y_max:
                    player.y += 1
                else:
                    player.y = 0
            case ['1']:
                player = item_shop(player)
            case ['2']:
                player = magic_shop(player)
            case ['3']:
                current_map, x_max, y_max = set_map(town_map)
                player.x = 0
                player.y = 0
            case ['4']:
                player = inn(player)
            case ['9']:
                current_map, x_max, y_max = set_map(starting_map)
                player.x = 3
                player.y = 2
            case _:
                input(error_msg)

print("Exiting")
time.sleep(5)
