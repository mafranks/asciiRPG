"""Main file for the ASCII RPG"""
import colorama
import random

import maps
from enemies import Enemy, enemy_list
from maps import starting_map, biomes, town_map
from pathlib import Path
from player import Player, use_inventory, print_player_info, use_magic, level_up_check
from shops import item_shop, magic_shop, inn
from utilities import clear, error_msg, line, main_map_line, town_line

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
standing = True  # Avoids fight change immediately upon start of game and while using menus

# colorama allows you to color text in the console
colorama.init()


def set_map(target_map):
    """Set the current map to use and provide map boundaries
    param: target_map The map that will be loaded
    """
    cur_map = target_map
    x__max = len(cur_map) - 1
    y__max = len(cur_map[0]) - 1
    return cur_map, x__max, y__max


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
    player_data = Player()

    def name_player(player_data):
        """Give the player a name"""
        name = input("What is your name? ")
        clear()
        if len(name) <= 2:
            print("Name must be 3 or more characters.")
            input("> ")
            name_player(player_data)
        else:
            player_data.name = name
    name_player(player_data)
    print(f"Welcome to the game, {player_data.name}!")
    return player_data


def main_menu(player_data, starting_map, town_map):
    """Prints menu options after the game has started
    :param player_data Player object
    :param starting_map The initial map for the game
    :param town_map Map of the town area"""
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
    print("0 - Go Back")
    print(f"{player_data.name}'s HP: {player_data.HP}/{player_data.MAXHP}")
    print(f"{player_data.name}'s MP: {player_data.MP}/{player_data.MAXMP}")
    choice = input("< ")
    match choice:
        case "1":
            clear()
            player_data = print_player_info(player_data)
        case "2":
            player_data, _ = use_inventory(player_data)
            clear()
        case "3":
            clear()
            print(f"{player.name} knows these battle spells: ")
            for spell in player.magic:
                if not spell.startswith('heal'):
                    print(f"\t{spell}")
            print(f"\n{player.name} knows these healing spells: ")
            for spell in player.magic:
                if spell.startswith('heal'):
                    print(f"\t{spell}")
            player_data, _, _ = use_magic(player_data)
            clear()
        case "4":
            save(player_data, [starting_map, town_map])
            input("> ")
        case "5":
            print("Are you sure you want to load a game?  This will overwrite your existing game! (Y/N)")
            choice2 = input("> ")
            match choice2.split():
                case ['Y'] | ['y']:
                    print("Loading Game")
                    player_data, starting_map, town_map = load()
                case ['N'] | ['n']:
                    main_menu(player_data, starting_map, town_map)
                case _:
                    input(error_msg)
        case "6":
            print("Are you sure you want to start a new game?  This will overwrite your existing game! (Y/N)")
            choice2 = input("> ")
            match choice2.split():
                case ['Y'] | ['y']:
                    print("Loading New Game")
                    player_data = create_new_player()
                case ['N'] | ['n']:
                    main_menu(player_data, starting_map, town_map)
                case _:
                    input(error_msg)
        case "7":
            print_rules()
        case "8" | 'q' | 'Q':
            intro = False
            play = False
            run = False
        case "0":
            clear()
        case _:
            input(error_msg)
            clear()
            main_menu(player_data, starting_map, town_map)

    return player_data


def save(player_data, maps: list):
    """Save the game to a local file
    :param player_data Player object to be saved
    :param maps List of all maps to be saved
    """

    # Add more maps as they are created
    starting_map = maps[0]
    town_map = maps[1]
    save_file = input("Enter a name for your save file: ")
    if Path(f"{save_file}.pkl").is_file():
        choice_ = input(f"A save named {save_file} already exists, do you want to overwrite it? (y/n) ")
        match choice_:
            case 'y':
                with open(f"saves/{save_file}.pkl", "wb") as file, \
                        open(f"saves/{save_file}_starting_map.pkl", "wb") as starting_map_file, \
                        open(f"saves/{save_file}_town_map.pkl", "wb") as town_map_file:
                    pickle.dump(player_data, file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(starting_map, starting_map_file, pickle.HIGHEST_PROTOCOL)
                    pickle.dump(town_map, town_map_file, pickle.HIGHEST_PROTOCOL)
            case 'n':
                save(player_data, [starting_map, town_map])
            case _:
                print("Input not understood.")
                save(player_data, [starting_map, town_map])
    else:
        with open(f"saves/{save_file}.pkl", "wb") as file, \
                open(f"saves/{save_file}_starting_map.pkl", "wb") as starting_map_file, \
                open(f"saves/{save_file}_town_map.pkl", "wb") as town_map_file:
            pickle.dump(player_data, file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(starting_map, starting_map_file, pickle.HIGHEST_PROTOCOL)
            pickle.dump(town_map, town_map_file, pickle.HIGHEST_PROTOCOL)
    print(f"Player data saved as {save_file}")


def load():
    """Loads the game from a local file.  Returns loaded player data."""
    global starting_map, town_map
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
        player_data = create_new_player()
        return player_data, starting_map, town_map

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
                player_data = pickle.load(save_file)
            with open(f"saves/{saves[choice_ - 1]}_starting_map.pkl", "rb") as starting_map_file:
                starting_map = pickle.load(starting_map_file)
            with open(f"saves/{saves[choice_ - 1]}_town_map.pkl", "rb") as town_map_file:
                town_map = pickle.load(town_map_file)
            clear()
            print(f"Welcome back {player_data.name}!")
            input("> ")
            return player_data, starting_map, town_map
        else:
            player_data = None
            clear()
            print("Please enter a number based on the list options.")
            input("> ")
    except ValueError:
        player_data = None
        clear()
        print("Please enter a number based on the list options.")
        input("> ")
    return player_data


def display_map(cur_map, player_data):
    """Displays the explored section of the current map
    :param cur_map Map to be displayed
    :param player_data Current player object to be displayed on the map
    """
    # Counts are needed to see if player is on that tile
    row_count = 0
    for row in range(len(cur_map)):
        if len(cur_map[0]) == 7:
            print(f"\n{main_map_line}")
        elif len(cur_map[0]) == 2:
            print(f"\n{town_line}")
        tile_count = 0
        for tile in cur_map[row]:
            if tile['visible'] is True:
                if (row_count, tile_count) == (player_data.x, player_data.y):
                    print(colorama.Fore.GREEN + f"{biomes[tile['type']]['display']} \033[39m",  end='')
                else:
                    print(f"{biomes[tile['type']]['display']} ",  end='')
            else:
                print('XXXXXXXXX| ', end='')
            tile_count += 1
        row_count += 1
    if len(cur_map[0]) == 7:
        print(f"\n{main_map_line}")
    elif len(cur_map[0]) == 2:
        print(f"\n{town_line}")


def battle(current_enemy, player_data):
    """Kicks of a battle sequence between the player and a randomly chosen enemy"""
    global fight, play, run, line
    enemy = Enemy(current_enemy)
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
            match action:
                case "1":
                    damage = random.randint(player_data.attack - 5, player_data.attack + 5)
                    enemy.hp -= damage
                    print(f"{player_data.name} dealt {damage} damage to the {enemy.name}")
                    break
                case "2":
                    player, enemy, action_taken = use_magic(player_data, fight, enemy)
                    clear()
                    if action_taken is True:
                        break
                case "3":
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
        match choice:
            case "1":
                setup = True
                intro = False
            case "2":
                player, starting_map, town_map = load()
                if player is None:
                    continue
                if player.map == 'starting_map':
                    current_map, x_max, y_max = set_map(starting_map)
                elif player.map == 'town_map':
                    current_map, x_max, y_max = set_map(town_map)
                intro = False
                setup = False
                play = True
            case "3":
                print_rules()
            case "4":
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

        display_map(current_map, player)
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
        destination = input("> ")
        if destination == "0":
            player = main_menu(player, starting_map, town_map)
        elif destination == "w" or destination == "W":
            standing = False
            if player.x > 0:
                player.x -= 1
            else:
                player.x = x_max
        elif destination == "S" or destination == "s":
            standing = False
            if player.x < x_max:
                player.x += 1
            else:
                player.x = 0
        elif destination == "A" or destination == "a":
            standing = False
            if player.y > 0:
                player.y -= 1
            else:
                player.y = y_max
        elif destination == "D" or destination == "d":
            standing = False
            if player.y < y_max:
                player.y += 1
            else:
                player.y = 0
        elif current_tile == 'item_shop' and destination == '1':
            player = item_shop(player)
            standing = True
        elif current_tile == 'magic_shop' and destination == '2':
            player = magic_shop(player)
            standing = True
        elif current_tile == 'town' and destination == '3':
            player.map = 'town_map'
            current_map, x_max, y_max = set_map(town_map)
            player.x = 0
            player.y = 0
        elif current_tile == 'inn' and destination == '4':
                player = inn(player)
        elif current_tile == 'entrance' and destination == '9' and player.map == 'town_map':
            player.map = 'starting_map'
            current_map, x_max, y_max = set_map(starting_map)
            player.x = 3
            player.y = 2
        else:
            input(error_msg)

print("Thanks for playing!")
