"""Player statistics and informaiton"""
from utilities import clear, error_msg


class Player:
    """Player object containing all the player related stats"""

    def __init__(self):
        self.name = ''
        self.HP = 50
        self.MAXHP = 50
        self.MP = 10
        self.MAXMP = 10
        self.attack = 10
        # TODO - Add more spells for purchase in the magic shop
        self.magic = ["fire", "heal"]
        self.gold = 0
        self.potions = 1
        self.mid_potions = 1
        self.high_potions = 1
        self.ethers = 1
        self.mid_ethers = 1
        self.high_ethers = 1
        self.x = 0
        self.y = 0


def print_player_info(player):
    """Print player information"""
    print(f"Name: {player.name}")
    print(f"HP: {player.HP}/{player.MAXHP}")
    print(f"MP: {player.MP}/{player.MAXMP}")
    print(f"Gold: {player.gold}")
    print(f"Attack: {player.attack}")
    print(f"Position: {player.x, player.y}")
    input("> ")
    return player


def print_items_list(player):
    """Print items held by the player"""
    print(f"Potions: {player.potions}")
    print(f"Mid-Potions: {player.mid_potions}")
    print(f"High-Potions: {player.high_potions}")
    print(f"Ethers: {player.ethers}")
    print(f"Mid-Ethers: {player.mid_ethers}")
    print(f"High-Ethers: {player.high_ethers}")


line = "--------------------"


def use_inventory(player):
    """Use available inventory items"""
    global error_msg
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
            print(error_msg)
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
    """Use magic spells"""
    print(line)
    if 'heal' in player.magic:
        print("1 - Heal: Cost 5MP, Heals 20HP")
    if 'fire' in player.magic and fight is True:
        print("2 - Fire: Cost 2MP, Damage 20HP")
    print("0 - Go back")
    choice = input("> ")
    match choice.split():
        case ["1"]:
            if player.MP > 5:
                print("Using Heal.....")
                player.MP -= 5
                player.HP += 20
                if player.HP > player.MAXHP:
                    player.HP = player.MAXHP
            else:
                print("Not enough MP to use this spell")
            print(line)
            print(f"{player.name}'s HP: {player.HP}/{player.MAXHP}")
            print(f"{player.name}'s MP: {player.MP}/{player.MAXMP}")
        case ["2"]:
            if player.MP > 2 and fight is True:
                print("Using fire.....")
                player.MP -= 2
                enemy.hp -= 20
            else:
                print("Not enough MP to use this spell")
            print(line)
            print(f"{enemy.name} took 20 damage.")
            if enemy.hp < 0:
                enemy.hp = 0
            print(f"Enemy HP: {enemy.hp}/{enemy.maxhp}")
        case ["0"]:
            return player, enemy, False
        case _:
            print(error_msg)
            use_magic(player, fight, enemy)
    input("> ")
    return player, enemy, True
