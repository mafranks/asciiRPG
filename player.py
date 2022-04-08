"""Player statistics and informaiton"""
import random
from utilities import clear, error_msg


levels = {
    1: {"xp_required": 0, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    2: {"xp_required": 50, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    3: {"xp_required": 120, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    4: {"xp_required": 200, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    5: {"xp_required": 310, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    6: {"xp_required": 500, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    7: {"xp_required": 750, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    8: {"xp_required": 1150, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    9: {"xp_required": 1500, "atk_up": random.randint(1, 5), "hp_up": random.randint(1, 5), "mp_up": random.randint(1, 5)},
    10: {"xp_required": 20000, "atk_up": random.randint(10, 50), "hp_up": random.randint(10, 50), "mp_up": random.randint(10, 50)}
}


def level_up_check(player):
    """Check to see if the player has leveled up"""
    if player.XP > levels[player.level + 1]['xp_required']:
        print(f"Congratulations!  You've leveled up!")
        player.level += 1
        print(f"{player.name} is now Level {player.level}")
        player.attack += levels[player.level]['atk_up']
        print(f"Attack increased by {levels[player.level]['atk_up']}")
        player.MAXHP += levels[player.level]['hp_up']
        print(f"Max HP increased by {levels[player.level]['hp_up']}")
        player.MAXMP += levels[player.level]['mp_up']
        print(f"Max MP increased by {levels[player.level]['atk_up']}")
    return player


class Player:
    """Player object containing all the player related stats"""

    def __init__(self):
        self.name = ''
        self.HP = 50
        self.MAXHP = 50
        self.MP = 10
        self.MAXMP = 10
        self.attack = 10
        self.magic = random.sample(["fire", "ice", "lightning", "heal"], 2)
        self.gold = 500
        self.potions = 1
        self.mid_potions = 1
        self.high_potions = 1
        self.ethers = 1
        self.mid_ethers = 1
        self.high_ethers = 1
        self.x = 0
        self.y = 0
        self.XP = 0
        self.level = 1


def print_player_info(player):
    """Print player information
    :param player Player object for the current game"""
    print(f"Name: {player.name}")
    print(f"Level: {player.level}")
    print(f"HP: {player.HP}/{player.MAXHP}")
    print(f"MP: {player.MP}/{player.MAXMP}")
    print(f"Gold: {player.gold}")
    print(f"Attack: {player.attack}")
    input("> ")
    return player


def print_items_list(player):
    """Print items held by the player
    :param player Player object for the current game"""
    print(f"Potions: {player.potions}")
    print(f"Mid-Potions: {player.mid_potions}")
    print(f"High-Potions: {player.high_potions}")
    print(f"Ethers: {player.ethers}")
    print(f"Mid-Ethers: {player.mid_ethers}")
    print(f"High-Ethers: {player.high_ethers}")


def magic_error(spell, player, enemy):
    """Display error if player tries to use a spell they either don't have or don't have enough MP to use
    :param spell Current spell the player is trying to use
    :param player Player object for the current game
    :param enemy Current enemy for the ongoing battle"""
    if spell not in player.magic:
        print(f"{player.name} has not learned {spell}. Please visit the Magic Shop.")
    else:
        print(f"{player.name} does not have enough MP to use this spell")
    input("> ")


line = "--------------------"


def use_inventory(player):
    """Use available inventory items
    :param player Player object for the current game"""
    clear()
    print(line)
    print("Inventory - Select which item to use")
    if player.potions > 0:
        print(f"1 - Potion: {player.potions}")
    if player.mid_potions > 0:
        print(f"2 - Mid Potion: {player.mid_potions}")
    if player.high_potions > 0:
        print(f"3 - High Potion: {player.high_potions}")
    if player.ethers > 0:
        print(f"4 - Ether: {player.ethers}")
    if player.mid_ethers > 0:
        print(f"5 - Mid Ether: {player.mid_ethers}")
    if player.high_ethers > 0:
        print(f"6 - High Ether: {player.high_ethers}")
    print("0 - Go back")
    choice = input("> ")
    match choice.split():
        case ["1"]:
            if player.potions > 0:
                player.HP += 10
                print(f"{player.name} regained 10 HP")
                player.potions -= 1
        case ["2"]:
            if player.mid_potions > 0:
                player.HP += 25
                print(f"{player.name} regained 25 HP")
                player.mid_potions -= 1
        case ["3"]:
            if player.high_potions > 0:
                player.HP += 50
                print(f"{player.name} regained 50 HP")
                player.high_potions -= 1
        case ["4"]:
            if player.ethers > 0:
                player.MP += 2
                print(f"{player.name} regained 2 MP")
                player.ethers -= 1
        case ["5"]:
            if player.mid_ethers > 0:
                player.MP += 5
                print(f"{player.name} regained 5 MP")
                player.mid_ethers -= 1
        case ["6"]:
            if player.high_ethers > 0:
                player.MP += 10
                print(f"{player.name} regained 10 MP")
                player.high_ethers -= 1
        case ["0"]:
            return player, False
        case _:
            input(error_msg)
            use_inventory(player)

    if player.HP > player.MAXHP:
        player.HP = player.MAXHP
    if player.MP > player.MAXMP:
        player.MP = player.MAXMP
    print(line)
    print(f"{player.name}'s HP: {player.HP}/{player.MAXHP}")
    print(f"{player.name}'s MP: {player.MP}/{player.MAXMP}")
    input("> ")
    return player, True


def use_magic(player, fight=False, enemy=None):
    """Use magic spells
    :param player Player object for the current game
    :param fight Boolean which indicates if a battle is taking place
    :param enemy Current enemy for ongoing battle"""
    print(line)
    if 'fire' in player.magic and fight is True:
        print("1 - Fire: Cost 2MP")
    if 'lightning' in player.magic and fight is True:
        print("2 - Lightning: Cost 2MP")
    if 'ice' in player.magic and fight is True:
        print("3 - Ice: Cost 2MP")
    if 'fire2' in player.magic and fight is True:
        print("4 - Fire2: Cost 5MP")
    if 'lightning2' in player.magic and fight is True:
        print("5 - Lightning2: Cost 5MP")
    if 'ice2' in player.magic and fight is True:
        print("6 - Ice2: Cost 5MP")
    if 'heal' in player.magic:
        print("7 - Heal: Cost 3MP, Heals some HP")
    if 'heal2' in player.magic:
        print("8 - Heal: Cost 6MP, Heals more HP")
    if 'heal3' in player.magic:
        print("9 - Heal: Cost 10MP, Heals all HP")
    print("0 - Go back")
    choice = input("> ")
    if choice == "1" and fight is True and 'fire' in player.magic:
        if player.MP >= 2:
            print("Using fire.....")
            player.MP -= 2
            dmg = random.randint(10, 25)
            if 'fire' in enemy.resistance:
                print(f"{enemy.name} is resistant to fire")
                hit = int(dmg * .75)
            elif 'fire' in enemy.immunity:
                print(f"{enemy.name} is immune to fire")
                hit = 0
            else:
                hit = dmg
            enemy.hp -= hit
        else:
            magic_error('fire', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "2" and fight is True and 'lightning' in player.magic:
        if player.MP >= 2:
            print("Using lighting.....")
            player.MP -= 2
            hit = random.randint(10, 25)
            enemy.hp -= hit
        else:
            magic_error('lightning', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "3" and fight is True and 'ice' in player.magic:
        if player.MP >= 2:
            print("Using ice.....")
            player.MP -= 2
            hit = random.randint(10, 25)
            enemy.hp -= hit
        else:
            magic_error('ice', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "4" and fight is True and 'fire2' in player.magic:
        if player.MP >= 5:
            print("Using Fire 2.....")
            player.MP -= 5
            hit = random.randint(30, 55)
            enemy.hp -= hit
        else:
            magic_error('fire2', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "5" and fight is True and 'lightning2' in player.magic:
        if player.MP >= 5:
            print("Using Lightning 2.....")
            player.MP -= 5
            hit = random.randint(30, 55)
            enemy.hp -= hit
        else:
            magic_error('lightning2', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "6" and fight is True and 'ice2' in player.magic:
        if player.MP >= 5:
            print("Using Ice 2.....")
            player.MP -= 5
            hit = random.randint(30, 55)
            enemy.hp -= hit
        else:
            magic_error('ice2', player, enemy)
            return player, enemy, False
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    elif choice == "7" and 'heal' in player.magic:
        if player.MP >= 3:
            print("Using Heal.....")
            player.MP -= 3
            heal = random.randint(15, 25)
            player.HP += heal
            print(line)
            print(f"{player.name} was healed {heal} HP.")
            if player.HP > player.MAXHP:
                player.HP = player.MAXHP
        else:
            magic_error('heal', player, enemy)
            return player, enemy, False
    elif choice == "8" and 'heal2' in player.magic:
        if player.MP >= 6:
            print("Using Heal 2.....")
            player.MP -= 6
            heal = random.randint(35, 65)
            player.HP += heal
            if player.HP > player.MAXHP:
                player.HP = player.MAXHP
            print(line)
            print(f"{player.name} was healed {heal} HP.")
        else:
            magic_error('heal2', player, enemy)
            return player, enemy, False
    elif choice == "9" and 'heal3' in player.magic:
        if player.MP >= 10:
            print("Using Heal 3.....")
            player.MP -= 10
            heal = player.MAXHP - player.HP
            player.HP = player.MAXHP
            print(line)
            print(f"{player.name} was healed {heal} HP.")
        else:
            magic_error('heal3', player, enemy)
            return player, enemy, False
    elif choice == "0":
        return player, enemy, False
    else:
        input(error_msg)
        use_magic(player, fight, enemy)
    print(f"{player.name}'s HP: {player.HP}/{player.MAXHP}")
    print(f"{player.name}'s MP: {player.MP}/{player.MAXMP}")
    input("> ")
    return player, enemy, True
