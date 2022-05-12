"""Player statistics and informaiton"""
import random
from utilities import clear, error_msg
from spells import spells


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

classes = {
    'tester': {
        'HP': 5000,
        'MAXHP': 5000,
        'MP': 1000,
        'MAXMP': 1000,
        'magic': ['heal', 'heal2', 'heal3', 'fire', 'fire2', 'ice', 'ice2', 'lightning', 'lightning2'],
        'gold': 5000,
        'potions': 100,
        'mid_potions': 100,
        'high_potions': 100,
        'ethers': 100,
        'mid_ethers': 100,
        'high_ethers': 100,
        'tents': 5,
        'attack': 100
    },
    'red_mage': {
        'HP': 40,
        'MAXHP': 40,
        'MP': 60,
        'MAXMP': 60,
        'magic': ['heal', 'fire'],
        'gold': 0,
        'potions': 1,
        'mid_potions': 0,
        'high_potions': 0,
        'ethers': 1,
        'mid_ethers': 0,
        'high_ethers': 0,
        'tents': 5,
        'attack': 8
    },
    'white_mage': {
        'HP': 40,
        'MAXHP': 40,
        'MP': 60,
        'MAXMP': 60,
        'magic': ['heal', 'heal2'],
        'gold': 0,
        'potions': 1,
        'mid_potions': 0,
        'high_potions': 0,
        'ethers': 1,
        'mid_ethers': 0,
        'high_ethers': 0,
        'tents': 5,
        'attack': 8
    },
    'barbarian': {
        'HP': 100,
        'MAXHP': 100,
        'MP': 0,
        'MAXMP': 0,
        'magic': [],
        'gold': 0,
        'potions': 1,
        'mid_potions': 0,
        'high_potions': 0,
        'ethers': 1,
        'mid_ethers': 0,
        'high_ethers': 0,
        'tents': 5,
        'attack': 20
    },
    'thief': {
        'HP': 60,
        'MAXHP': 60,
        'MP': 30,
        'MAXMP': 30,
        'magic': ['lightning'],
        'gold': 0,
        'potions': 1,
        'mid_potions': 0,
        'high_potions': 0,
        'ethers': 1,
        'mid_ethers': 0,
        'high_ethers': 0,
        'tents': 5,
        'attack': 8
    },
    'blue_mage': {
        'HP': 40,
        'MAXHP': 40,
        'MP': 60,
        'MAXMP': 60,
        'magic': ['heal', 'ice'],
        'gold': 0,
        'potions': 1,
        'mid_potions': 0,
        'high_potions': 0,
        'ethers': 1,
        'mid_ethers': 0,
        'high_ethers': 0,
        'tents': 5,
        'attack': 8
    }
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

    def __init__(self, player_type):
        self.name = ''
        self.HP = classes[player_type]['HP']
        self.MAXHP = classes[player_type]['MAXHP']
        self.MP = classes[player_type]['MP']
        self.MAXMP = classes[player_type]['MAXMP']
        self.magic = classes[player_type]['magic']
        self.gold = classes[player_type]['gold']
        self.potions = classes[player_type]['potions']
        self.mid_potions = classes[player_type]['mid_potions']
        self.high_potions = classes[player_type]['high_potions']
        self.ethers = classes[player_type]['ethers']
        self.mid_ethers = classes[player_type]['mid_ethers']
        self.high_ethers = classes[player_type]['high_ethers']
        self.tents = classes[player_type]['tents']
        self.attack = classes[player_type]['attack']
        self.player_type = player_type
        self.x = 0
        self.y = 0
        self.XP = 0
        self.level = 1
        self.clayton = False
        self.key = False
        self.won = False


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


def print_items_list(player):
    """Print items held by the player
    :param player Player object for the current game"""
    print(f"Potions: {player.potions}")
    print(f"Mid-Potions: {player.mid_potions}")
    print(f"High-Potions: {player.high_potions}")
    print(f"Ethers: {player.ethers}")
    print(f"Mid-Ethers: {player.mid_ethers}")
    print(f"High-Ethers: {player.high_ethers}")


def magic_error(spell, player):
    """Display error if player tries to use a spell they either don't have or don't have enough MP to use
    :param spell Current spell the player is trying to use
    :param player Player object for the current game"""
    if spell not in player.magic:
        print(f"{player.name} has not learned {spell}. Please visit the Magic Shop.")
    else:
        print(f"{player.name} does not have enough MP to use this spell")
    input("> ")


line = "--------------------"


def use_inventory(player, fight=False):
    """Use available inventory items
    :param player Player object for the current game
    :param fight True if player is in a battle"""
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
    if player.tents > 0 and fight is False:
        print(f"7 - Tent: {player.tents}")
    print("0 - Go back")
    choice = input("> ")
    match choice:
        case "1":
            if player.potions > 0:
                amount = player.HP / 4
                player.HP += amount
                print(f"{player.name} regained {amount} HP")
                player.potions -= 1
        case "2":
            if player.mid_potions > 0:
                amount = player.HP / 2
                player.HP += amount
                print(f"{player.name} regained {amount} HP")
                player.mid_potions -= 1
        case "3":
            if player.high_potions > 0:
                amount = player.MAXHP - player.HP
                player.HP = player.MAXHP
                print(f"{player.name} regained {amount} HP")
                player.high_potions -= 1
        case "4":
            if player.ethers > 0:
                amount = player.MP / 4
                player.MP += amount
                print(f"{player.name} regained {amount} MP")
                player.ethers -= 1
        case "5":
            if player.mid_ethers > 0:
                amount = player.MP / 2
                player.MP += amount
                print(f"{player.name} regained {amount} MP")
                player.mid_ethers -= 1
        case "6":
            if player.high_ethers > 0:
                amount = player.MAXMP - player.MP
                player.MP += amount
                print(f"{player.name} regained {amount} MP")
                player.high_ethers -= 1
        case "7":
            if player.tents > 0 and fight is False:
                player.HP = player.MAXHP
                player.MP = player.MAXMP
                player.tents -= 1
        case "0":
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


def use_spell(player, enemy, spell):
    """Process the damage/heal effect of a spell
    :param player Player object for the current game
    :param enemy Enemy object or the current battle
    :param spell Spell being used"""
    print(f"Using {spell}.....")
    player.MP -= spells[spell]['MP_Cost']
    # If attacking spell
    if not spell.startswith('heal'):
        dmg = random.randint(spells[spell]['Damage_Min'], spells[spell]['Damage_Max'])
        if spell in enemy.resistance:
            print(f"{enemy.name} is resistant to {spell}.")
            hit = int(dmg * .75)
        elif spell in enemy.immunity:
            print(f"{enemy.name} is immune to {spell}.")
            hit = 0
        else:
            hit = dmg
        enemy.hp -= hit
        print(line)
        print(f"{enemy.name} took {hit} damage.")
        if enemy.hp < 0:
            enemy.hp = 0
        print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
    # If healing spell
    else:
        player.MP -= spells[spell]['MP_Cost']
        if spell == 'heal3':
            player.HP = player.MAXHP
            print(line)
            print(f"{player.name} was healed {player.MAXHP} HP.")
        else:
            heal = random.randint(spells[spell]['Heal_Min'], spells[spell]['Heal_Max'])
            player.HP += heal
            print(line)
            print(f"{player.name} was healed {heal} HP.")
        if player.HP > player.MAXHP:
            player.HP = player.MAXHP
    return player, enemy


def use_magic(player, fight=False, enemy=None):
    """Use magic spells
    :param player Player object for the current game
    :param fight Boolean which indicates if a battle is taking place
    :param enemy Current enemy for ongoing battle"""
    print(line)
    if 'fire' in player.magic and fight is True:
        print(f"1 - Fire: Cost {spells['fire']['MP_Cost']}")
    if 'lightning' in player.magic and fight is True:
        print(f"2 - Lightning: Cost {spells['lightning']['MP_Cost']}")
    if 'ice' in player.magic and fight is True:
        print(f"3 - Ice: Cost {spells['ice']['MP_Cost']}")
    if 'fire2' in player.magic and fight is True:
        print(f"4 - Fire2: Cost {spells['fire2']['MP_Cost']}")
    if 'lightning2' in player.magic and fight is True:
        print(f"5 - Lightning2: Cost {spells['lightning2']['MP_Cost']}")
    if 'ice2' in player.magic and fight is True:
        print(f"6 - Ice2: Cost {spells['ice2']['MP_Cost']}")
    if 'heal' in player.magic:
        print(f"7 - Heal: Cost {spells['heal']['MP_Cost']}, Heals some HP")
    if 'heal2' in player.magic:
        print(f"8 - Heal2: Cost {spells['heal2']['MP_Cost']}, Heals more HP")
    if 'heal3' in player.magic:
        print(f"9 - Heal3: Cost {spells['heal3']['MP_Cost']}, Heals all HP")
    print("0 - Go back")
    choice = input("> ")
    if choice == "1" and fight is True and 'fire' in player.magic:
        if player.MP >= spells['fire']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'fire')
        else:
            magic_error('fire', player)
            return player, enemy, False
    elif choice == "2" and fight is True and 'lightning' in player.magic:
        if player.MP >= spells['lightning']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'lightning')
        else:
            magic_error('lightning', player)
            return player, enemy, False
    elif choice == "3" and fight is True and 'ice' in player.magic:
        if player.MP >= spells['ice']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'ice')
        else:
            magic_error('ice', player)
            return player, enemy, False
    elif choice == "4" and fight is True and 'fire2' in player.magic:
        if player.MP >= spells['fire2']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'fire2')
        else:
            magic_error('fire2', player)
            return player, enemy, False
    elif choice == "5" and fight is True and 'lightning2' in player.magic:
        if player.MP >= spells['lightning2']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'lightning2')
        else:
            magic_error('lightning2', player)
            return player, enemy, False
    elif choice == "6" and fight is True and 'ice2' in player.magic:
        if player.MP >= spells['ice2']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'ice2')
        else:
            magic_error('ice2', player)
            return player, enemy, False
    elif choice == "7" and 'heal' in player.magic:
        if player.MP >= spells['heal']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'heal')
        else:
            magic_error('heal', player)
            return player, enemy, False
    elif choice == "8" and 'heal2' in player.magic:
        if player.MP >= spells['heal2']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'heal2')
        else:
            magic_error('heal2', player)
            return player, enemy, False
    elif choice == "9" and 'heal3' in player.magic:
        if player.MP >= spells['heal3']['MP_Cost']:
            player, enemy = use_spell(player, enemy, 'heal3')
        else:
            magic_error('heal3', player)
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
