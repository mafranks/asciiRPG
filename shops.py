"""Shop functions for magic and items"""
from utilities import line, clear, error_msg
from spells import spells


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
    clear()
    print(line)
    print("MAGIC SHOP:")
    if 'fire' not in player.magic:
        print(f"1. {spells['Fire']['Purchase']} Gold: Fire - Fire Attack")
    if 'fire2' not in player.magic:
        print(f"2. {spells['Fire2']['Purchase']} Gold: Fire 2 - Advanced Fire Attack")
    if 'ice' not in player.magic:
        print(f"3. {spells['Ice']['Purchase']} Gold: Ice - Ice Attack")
    if 'ice2' not in player.magic:
        print(f"4. {spells['Ice2']['Purchase']} Gold: Ice 2 - Advanced Ice Attack")
    if 'lightning' not in player.magic:
        print(f"5. {spells['Lightning']['Purchase']} Gold: Lightning - Lightning Attack")
    if 'lightning2' not in player.magic:
        print(f"6. {spells['Lightning2']['Purchase']} Gold: Lightning 2 - Advanced Lightning Attack")
    if 'heal' not in player.magic:
        print(f"7. {spells['Heal']['Purchase']} Gold: Heal - Heals 20 HP")
    if 'heal2' not in player.magic:
        print(f"8. {spells['Heal2']['Purchase']} Gold: Heal 2 - Heals 50 HP")
    if 'heal3' not in player.magic:
        print(f"9. {spells['Heal3']['Purchase']} Gold: Heal 3 - Fully heals player")
    if len(player.magic) == 9:
        print("Congratulations, you have purchased all available spells!")
    print("0. Go back")
    print(line)
    return player


def magic_buy_error(player, cost):
    if player.gold < cost:
        print(not_enough)
    else:
        print("Unknown error occurred.")
    return player


def magic_buy(player, cost, spell):
    print(f"Purchasing Fire for {cost} Gold.")
    player.magic.append(spell)
    player.gold -= cost
    return player

def magic_shop(player):
    """Buy magic spells"""
    player = magic_menu(player)
    print(f"You have {player.gold} Gold available.")
    choice = input("< ")
    if choice == "1" and 'fire' not in player.magic:
        if player.gold >= spells['Fire']['Purchase']:
            player = magic_buy(player, spells['Fire']['Purchase'], "fire")
        else:
            player = magic_buy_error(player, spells['Fire']['Purchase'])
        input("> ")
        clear()
    elif choice == "2" and 'fire2' not in player.magic:
        if player.gold >= spells['Fire2']['Purchase']:
            player = magic_buy(player, spells['Fire2']['Purchase'], "fire2")
        else:
            player = magic_buy_error(player, spells['Fire2']['Purchase'])
        input("> ")
        clear()
    elif choice == "3" and 'ice' not in player.magic:
        if player.gold >= spells['Ice']['Purchase']:
            player = magic_buy(player, spells['Ice']['Purchase'], "ice")
        else:
            player = magic_buy_error(player, spells['Ice']['Purchase'])
        input("> ")
        clear()
    elif choice == "4" and 'ice2' not in player.magic:
        if player.gold >= spells['Ice2']['Purchase']:
            player = magic_buy(player, spells['Ice2']['Purchase'], "ice2")
        else:
            player = magic_buy_error(player, spells['Ice2']['Purchase'])
        input("> ")
        clear()
    elif choice == "5" and 'lightning' not in player.magic:
        if player.gold >= spells['Lightning']['Purchase']:
            player = magic_buy(player, spells['Lightning']['Purchase'], "lightning")
        else:
            player = magic_buy_error(player, spells['Lightning']['Purchase'])
        input("> ")
        clear()
    elif choice == "6" and 'lightning2' not in player.magic:
        if player.gold >= spells['Lightning2']['Purchase']:
            player = magic_buy(player, spells['Lightning2']['Purchase'], "lightning2")
        else:
            player = magic_buy_error(player, spells['Lightning2']['Purchase'])
        input("> ")
        clear()
    elif choice == "7" and 'heal' not in player.magic:
        if player.gold >= spells['Heal']['Purchase']:
            player = magic_buy(player, spells['Heal']['Purchase'], "heal")
        else:
            player = magic_buy_error(player, spells['Heal']['Purchase'])
        input("> ")
        clear()
    elif choice == "8" and 'heal2' not in player.magic:
        if player.gold >= spells['Heal2']['Purchase']:
            player = magic_buy(player, spells['Heal2']['Purchase'], "heal2")
        else:
            player = magic_buy_error(player, spells['Heal']['Purchase'])
        input("> ")
        clear()
    elif choice == "9" and 'heal3' not in player.magic:
        if player.gold >= spells['Heal3']['Purchase']:
            player = magic_buy(player, spells['Heal3']['Purchase'], "heal3")
        else:
            player = magic_buy_error(player, spells['Heal3']['Purchase'])
        input("> ")
        clear()
    elif choice == "0":
        clear()
        return player
    else:
        input(error_msg)

    return player


def inn(player):
    """Print menu for inn"""
    print(line)
    print("INN:")
    choice = input("Would you like to stay at the inn for 15 Gold (y/n) ?  ")
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
        case _:
            input(error_msg)

    return player
