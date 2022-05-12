"""Main file for the ASCII RPG"""
import colorama
import random

import maps
from enemies import enemy_list, enemy_stats
from game import Game
from shops import item_shop, magic_shop, inn
from utilities import clear, error_msg

# colorama allows you to color text in the console
colorama.init()

game = Game()

while game.run:
    while game.intro:
        clear()
        game.print_start_menu()

    while game.setup:
        clear()
        game.create_new_player()
        clear()
        game.name_player()
        input(f"Welcome to the game, {game.player.name}!")
        game.set_map(game.starting_map)
        game.play = True
        game.setup = False

    while game.play:
        clear()
        game.current_tile = game.current_map[game.player.x][game.player.y]['type']
        game.current_map[game.player.x][game.player.y]['visible'] = True
        if not game.standing and maps.biomes[game.current_tile]['enemies'] and random.randint(0, 100) < 25:
            game.fight = True
            enemy = enemy_list[random.randrange(0, len(enemy_list) - 1)]
            game.battle(enemy)

        game.display_map()
        print(f"Move with W,S,A,D")
        print(f"0 to view menu")
        if game.current_tile == 'item_shop':
            print(f"1 to visit the Item Shop")
        elif game.current_tile == 'magic_shop':
            print(f"2 to visit the Magic Shop")
        elif game.current_tile == 'town':
            print(f"3 to visit the Town")
        elif game.current_tile == 'inn':
            print(f"4 to visit the Inn")
        elif game.current_tile == 'cave':
            print(f"5 to enter the Cave")
        elif game.current_tile == 'castle':
            print(f"6 to enter the castle")
        elif game.current_tile == 'clayton':
            print(f"7 to speak with Clayton")
        elif game.current_tile == 'tower_door':
            print(f"8 to enter the tower")
        elif game.current_tile == 'entrance':
            print(f"9 to return to map")

        destination = input("> ")
        if destination == "0":
            game.main_menu()
        elif destination == "w" or destination == "W":
            game.standing = False
            if game.player.x > 0:
                game.player.x -= 1
            else:
                game.player.x = game.x_max
        elif destination == "S" or destination == "s":
            game.standing = False
            if game.player.x < game.x_max:
                game.player.x += 1
            else:
                game.player.x = 0
        elif destination == "A" or destination == "a":
            game.standing = False
            if game.player.y > 0:
                game.player.y -= 1
            else:
                game.player.y = game.y_max
        elif destination == "D" or destination == "d":
            game.standing = False
            if game.player.y < game.y_max:
                game.player.y += 1
            else:
                game.player.y = 0
        elif game.current_tile == 'item_shop' and destination == '1':
            game.player = item_shop(game.player)
            game.standing = True
        elif game.current_tile == 'magic_shop' and destination == '2':
            game.player = magic_shop(game.player)
            game.standing = True
        elif game.current_tile == 'town' and destination == '3':
            game.set_map(game.town_map)
            game.player.x = 0
            game.player.y = 0
        elif game.current_tile == 'inn' and destination == '4':
            game.player = inn(game.player)
        elif game.current_tile == 'cave' and destination == '5':
            game.set_map(game.cave_map)
            game.player.x = 0
            game.player.y = 0
        elif game.current_tile == 'castle' and destination == '6':
            game.set_map(game.castle_map)
            game.player.x = 0
            game.player.y = 0
        elif game.current_tile == 'clayton' and destination == '7':
            game.talk_to_clayton()
        elif game.current_tile == 'tower_door' and destination == '8':
            if game.player.key:
                input("You try to open the door but it seems to be locked.")
                input("You take out the key Clayton gave you and it slides smoothly into the lock.")
                input("A cool breeze hits your face as you open the door revealing a staircase.")
                choice = input("Do you want to enter and face the wizard? (y/n)")
                match choice:
                    case "y" | "Y":
                        input("This is it you whisper to yourself.")
                        input("Either I save the town or my body will lie on these cold stones forever.")
                        game.fight = True
                        game.battle('Wizard')
                        game.player.won = True
                    case "n" | "N":
                        input("You mumble something about forgetting your lucky socks and lock the door.")
                    case _:
                        input("Choice not understood. Try again with y or n.")
            else:
                input(f"You try to open the door but it seems to be locked.  You look around but don't see a key.")
        elif game.current_tile == 'entrance' and destination == '9' and game.current_map == game.town_map:
            game.set_map(game.starting_map)
            game.player.x = 3
            game.player.y = 2
        elif game.current_tile == 'entrance' and destination == '9' and game.current_map == game.cave_map:
            game.set_map(game.starting_map)
            game.player.x = 0
            game.player.y = 6
        elif game.current_tile == 'entrance' and destination == '9' and game.current_map == game.castle_map:
            game.set_map(game.starting_map)
            game.player.x = 3
            game.player.y = 3
        else:
            input(error_msg)

print("Thanks for playing!")
