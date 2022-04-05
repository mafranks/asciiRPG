"""Shop functions for magic and items"""
from utilities import line, clear, error_msg


not_enough = "You do not have sufficient Gold to purchase this item."


def item_menu():
    """Print item menu for item shop"""
    print(line)
    print("ITEM SHOP:")
    print("1. 5 Gold: Potion - Heals 10 HP")
    print("2. 15 Gold: Mid-Potion - Heals 25 HP")
    print("3. 30 Gold: High-Potion - Heals 50 HP")
    print("4. 10 Gold: Ether - Heals 2 MP")
    print("5. 20 Gold: Mid-Ether - Heals 5 MP")
    print("6. 40 Gold: High-Ether - Heals 10 MP")
    print("0. Go back")
    print(line)


def item_shop(player):
    """Buy and sell items"""
    item_menu()
    print(f"You have {player.gold} Gold available.")
    choice = input("< ")
    match choice.split():
        case ["1"]:
            if player.gold >= 5:
                print("Purchasing Potion for 5 Gold.")
                player.potions += 1
                player.gold -= 5
            else:
                input(not_enough)
            clear()
        case ["2"]:
            if player.gold >= 15:
                print("Purchasing Mid-Potion for 15 Gold.")
                player.mid_potions += 1
                player.gold -= 15
            else:
                input(not_enough)
            clear()
        case ["3"]:
            if player.gold >= 30:
                print("Purchasing High-Potion for 30 Gold.")
                player.high_potions += 1
                player.gold -= 30
            else:
                input(not_enough)
            clear()
        case ["4"]:
            if player.gold >= 10:
                print("Purchasing Ether for 10 Gold.")
                player.ethers += 1
                player.gold -= 10
            else:
                input(not_enough)
            clear()
        case ["5"]:
            if player.gold >= 20:
                print("Purchasing Mid-Ether for 20 Gold.")
                player.mid_ethers += 1
                player.gold -= 20
            else:
                input(not_enough)
            clear()
        case ["6"]:
            if player.gold >= 40:
                print("Purchasing High-Ether for 40 Gold.")
                player.high_ethers += 1
                player.gold -= 40
            else:
                input(not_enough)
            clear()
        case ["0"]:
            clear()
            return player
        case _:
            input(error_msg)

    return player


def magic_menu(player):
    """Print menu for magic shop"""
    print(line)
    print("MAGIC SHOP:")
    if 'fire' not in player.magic:
        print("1. 50 Gold: Fire - Fire Attack")
    if 'fire2' not in player.magic:
        print("2. 100 Gold: Fire 2 - Advanced Fire Attack")
    if 'ice' not in player.magic:
        print("3. 50 Gold: Ice - Ice Attack")
    if 'ice2' not in player.magic:
        print("4. 100 Gold: Ice 2 - Advanced Ice Attack")
    if 'lightning' not in player.magic:
        print("5. 50 Gold: Lightning - Lightning Attack")
    if 'lightning2' not in player.magic:
        print("6. 100 Gold: Lightning 2 - Advanced Lightning Attack")
    if 'heal' not in player.magic:
        print("7. 50 Gold: Heal - Heals 20 HP")
    if 'heal2' not in player.magic:
        print("8. 100 Gold: Heal 2 - Heals 50 HP")
    if 'heal3' not in player.magic:
        print("9. 250 Gold: Heal 3 - Fully heals player")
    print("0. Go back")
    print(line)
    return player


def magic_buy_error(player, spell, cost):
    if spell in player.magic:
        print(f"{player.name} already knows {spell}.")
    elif player.gold < cost:
        print(not_enough)
    else:
        print("Unknown error occurred.")
    return player


def magic_shop(player):
    """Buy magic spells"""
    player = magic_menu(player)
    print(f"You have {player.gold} Gold available.")
    choice = input("< ")
    match choice.split():
        case ["1"]:
            if player.gold >= 50 and 'fire' not in player.magic:
                print("Purchasing Fire for 50 Gold.")
                player.magic.append("fire")
                player.gold -= 50
            else:
                player = magic_buy_error(player, 'fire', 50)
            input("> ")
            clear()
        case ["2"]:
            if player.gold >= 100 and 'fire2' not in player.magic:
                print("Purchasing Fire 2 for 100 Gold.")
                player.magic.append("fire2")
                player.gold -= 100
            else:
                player = magic_buy_error(player, 'fire2', 100)
            input("> ")
            clear()
        case ["3"]:
            if player.gold >= 50 and 'ice' not in player.magic:
                print("Purchasing Ice for 50 Gold.")
                player.magic.append("ice")
                player.gold -= 50
            else:
                player = magic_buy_error(player, 'ice', 50)
            input("> ")
            clear()
        case ["4"]:
            if player.gold >= 100 and 'ice2' not in player.magic:
                print("Purchasing Ice 2 for 100 Gold.")
                player.magic.append("ice2")
                player.gold -= 100
            else:
                player = magic_buy_error(player, 'ice2', 100)
            input("> ")
            clear()
        case ["5"]:
            if player.gold >= 50 and 'lightning' not in player.magic:
                print("Purchasing Lightning for 50 Gold.")
                player.magic.append("lightning")
                player.gold -= 50
            else:
                player = magic_buy_error(player, 'lightning', 50)
            input("> ")
            clear()
        case ["6"]:
            if player.gold >= 100 and 'lightning2' not in player.magic:
                print("Purchasing Lightning 2 for 100 Gold.")
                player.magic.append("lightning2")
                player.gold -= 100
            else:
                player = magic_buy_error(player, 'lightning2', 100)
            input("> ")
            clear()
        case ["7"]:
            if player.gold >= 50 and 'heal' not in player.magic:
                print("Purchasing Heal for 50 Gold.")
                player.magic.append("heal")
                player.gold -= 50
            else:
                player = magic_buy_error(player, 'heal', 50)
            input("> ")
            clear()
        case ["8"]:
            if player.gold >= 100 and 'heal2' not in player.magic:
                print("Purchasing Heal 2 for 100 Gold.")
                player.magic.append("heal2")
                player.gold -= 100
            else:
                player = magic_buy_error(player, 'heal2', 100)
            input("> ")
            clear()
        case ["9"]:
            if player.gold >= 250 and 'heal3' not in player.magic:
                print("Purchasing Heal 3 for 50 Gold.")
                player.magic.append("heal3")
                player.gold -= 250
            else:
                player = magic_buy_error(player, 'heal3', 250)
            input("> ")
            clear()
        case ["0"]:
            clear()
            return player
        case _:
            input(error_msg)

    return player


def inn(player):
    """Print menu for inn"""
    print(line)
    print("INN:")
    choice = input("Would you like to stay at the inn for 15 Gold? y/n")
    match  choice.split():
        case ['y'] | ['Y'] | ['Yes'] | ['yes']:
            if player.gold >= 15:
                player.HP = player.MAXHP
                player.MP = player.MAXMP
                player.gold -= 15
                print("HP and MP restored")
                print(f"{player.name}'s HP: {player.HP}/{player.MAXHP}")
                print(f"{player.name}'s MP: {player.MP}/{player.MAXMP}")
                input("> ")
            else:
                print("Not enough Gold to stay at the Inn.")
        case ['n'] | ['N'] | ['No'] | ['no']:
            print("Please come again!")

    return player
