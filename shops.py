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
    print("7. 250 Gold: Tent - Fully heals HP and MP")
    print("0. Go back")
    print(line)


def item_shop(player):
    """Buy and sell items
    :param player Player object of the current player"""
    item_menu()
    print(f"You have {player.gold} Gold available.")
    choice = input("< ")
    match choice:
        case "1":
            if player.gold >= 5:
                print("Purchasing Potion for 5 Gold.")
                player.potions += 1
                player.gold -= 5
                input("> ")
            else:
                input(not_enough)
            clear()
        case "2":
            if player.gold >= 15:
                print("Purchasing Mid-Potion for 15 Gold.")
                player.mid_potions += 1
                player.gold -= 15
                input("> ")
            else:
                input(not_enough)
            clear()
        case "3":
            if player.gold >= 30:
                print("Purchasing High-Potion for 30 Gold.")
                player.high_potions += 1
                player.gold -= 30
                input("> ")
            else:
                input(not_enough)
            clear()
        case "4":
            if player.gold >= 10:
                print("Purchasing Ether for 10 Gold.")
                player.ethers += 1
                player.gold -= 10
                input("> ")
            else:
                input(not_enough)
            clear()
        case "5":
            if player.gold >= 20:
                print("Purchasing Mid-Ether for 20 Gold.")
                player.mid_ethers += 1
                player.gold -= 20
                input("> ")
            else:
                input(not_enough)
            clear()
        case "6":
            if player.gold >= 40:
                print("Purchasing High-Ether for 40 Gold.")
                player.high_ethers += 1
                player.gold -= 40
                input("> ")
            else:
                input(not_enough)
            clear()
        case "7":
            if player.gold >= 250:
                print("Purchasing Tent for 250 Gold.")
                player.tent += 1
                player.gold -= 250
                input("> ")
            else:
                input(not_enough)
            clear()
        case "0":
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
        print(f"1. {spells['fire']['Purchase']} Gold: Fire - Fire Attack")
    if 'fire2' not in player.magic:
        print(f"2. {spells['fire2']['Purchase']} Gold: Fire 2 - Advanced Fire Attack")
    if 'ice' not in player.magic:
        print(f"3. {spells['ice']['Purchase']} Gold: Ice - Ice Attack")
    if 'ice2' not in player.magic:
        print(f"4. {spells['ice2']['Purchase']} Gold: Ice 2 - Advanced Ice Attack")
    if 'lightning' not in player.magic:
        print(f"5. {spells['lightning']['Purchase']} Gold: Lightning - Lightning Attack")
    if 'lightning2' not in player.magic:
        print(f"6. {spells['lightning2']['Purchase']} Gold: Lightning 2 - Advanced Lightning Attack")
    if 'heal' not in player.magic:
        print(f"7. {spells['heal']['Purchase']} Gold: Heal - Heals 20 HP")
    if 'heal2' not in player.magic:
        print(f"8. {spells['heal2']['Purchase']} Gold: Heal 2 - Heals 50 HP")
    if 'heal3' not in player.magic:
        print(f"9. {spells['heal3']['Purchase']} Gold: Heal 3 - Fully heals player")
    if len(player.magic) == 9:
        print("Congratulations, you have purchased all available spells!")
    print("0. Go back")
    print(line)
    return player


def magic_buy_error(player, cost):
    """If funds are not sufficient to buy a magic spell, show an error
    :param player Player object for the current player
    :param cost Cost for the current spell"""
    if player.gold < cost:
        print(not_enough)
    else:
        print("Unknown error occurred.")
    return player


def magic_buy(player, cost, spell):
    """Purchase a spell
    :param player Player object of current player
    :param cost Cost of the spell
    :param spell Which spell is being purchased"""
    print(f"Purchasing {spell} for {cost} Gold.")
    player.magic.append(spell)
    player.gold -= cost
    return player


def magic_shop(player):
    """Buy magic spells
    :param player Player object of the current player"""
    player = magic_menu(player)
    print(f"You have {player.gold} Gold available.")
    choice = input("< ")
    if choice == "1" and 'fire' not in player.magic:
        if player.gold >= spells['fire']['Purchase']:
            player = magic_buy(player, spells['fire']['Purchase'], "fire")
        else:
            player = magic_buy_error(player, spells['fire']['Purchase'])
        input("> ")
        clear()
    elif choice == "2" and 'fire2' not in player.magic:
        if player.gold >= spells['fire2']['Purchase']:
            player = magic_buy(player, spells['fire2']['Purchase'], "fire2")
        else:
            player = magic_buy_error(player, spells['fire2']['Purchase'])
        input("> ")
        clear()
    elif choice == "3" and 'ice' not in player.magic:
        if player.gold >= spells['ice']['Purchase']:
            player = magic_buy(player, spells['ice']['Purchase'], "ice")
        else:
            player = magic_buy_error(player, spells['ice']['Purchase'])
        input("> ")
        clear()
    elif choice == "4" and 'ice2' not in player.magic:
        if player.gold >= spells['ice2']['Purchase']:
            player = magic_buy(player, spells['ice2']['Purchase'], "ice2")
        else:
            player = magic_buy_error(player, spells['ice2']['Purchase'])
        input("> ")
        clear()
    elif choice == "5" and 'lightning' not in player.magic:
        if player.gold >= spells['lightning']['Purchase']:
            player = magic_buy(player, spells['lightning']['Purchase'], "lightning")
        else:
            player = magic_buy_error(player, spells['lightning']['Purchase'])
        input("> ")
        clear()
    elif choice == "6" and 'lightning2' not in player.magic:
        if player.gold >= spells['lightning2']['Purchase']:
            player = magic_buy(player, spells['lightning2']['Purchase'], "lightning2")
        else:
            player = magic_buy_error(player, spells['lightning2']['Purchase'])
        input("> ")
        clear()
    elif choice == "7" and 'heal' not in player.magic:
        if player.gold >= spells['heal']['Purchase']:
            player = magic_buy(player, spells['heal']['Purchase'], "heal")
        else:
            player = magic_buy_error(player, spells['heal']['Purchase'])
        input("> ")
        clear()
    elif choice == "8" and 'heal2' not in player.magic:
        if player.gold >= spells['heal2']['Purchase']:
            player = magic_buy(player, spells['heal2']['Purchase'], "heal2")
        else:
            player = magic_buy_error(player, spells['heal2']['Purchase'])
        input("> ")
        clear()
    elif choice == "9" and 'heal3' not in player.magic:
        if player.gold >= spells['heal3']['Purchase']:
            player = magic_buy(player, spells['heal3']['Purchase'], "heal3")
        else:
            player = magic_buy_error(player, spells['heal3']['Purchase'])
        input("> ")
        clear()
    elif choice == "0":
        clear()
        return player
    else:
        input(error_msg)

    return player


def inn(player):
    """Print menu for inn
    :param player Player object of the current player"""
    print(line)
    print("INN:")
    choice = input("Would you like to stay at the inn for 15 Gold (y/n) ?  ")
    match  choice:
        case 'y' | 'Y' | 'Yes' | 'yes':
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
        case 'n' | 'N' | 'No' | 'no':
            print("Please come again!")
        case _:
            input(error_msg)

    return player
