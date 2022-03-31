"""Contains the various enemies and their statistics"""
import random
# TODO - Add enemies and randomize drops
enemy_list = ["Goblin", "Orc", "Slime"]


class Enemy:
    """Object containing all of the enemy data"""
    # TODO - Add enemy weaknesses and strengths (vs attack, magic types)
    def __init__(self, enemy):
        self.name = enemy_stats[enemy]['Name']
        self.hp = enemy_stats[enemy]['HP'],
        self.maxhp = enemy_stats[enemy]['MAXHP'],
        self.attack = enemy_stats[enemy]['Attack'],
        self.gold = random.randint(enemy_stats[enemy]['Gold'][0], enemy_stats[enemy]['Gold'][1])
        self.xp = random.randint(enemy_stats[enemy]['XP'][0], enemy_stats[enemy]['XP'][1])


enemy_stats = {
    "Slime": {
        "Name": "Slime",
        "HP": 15,
        "MAXHP": 15,
        "Attack": 2,
        "Gold": [5, 12],
        "XP": [10, 20]
    },
    "Goblin": {
        "Name": "Goblin",
        "HP": 25,
        "MAXHP": 25,
        "Attack": 5,
        "Gold": [8, 20],
        "XP": [25, 40]
    },
    "Orc": {
        "Name": "Orc",
        "HP": 30,
        "MAXHP": 30,
        "Attack": 2,
        "Gold": [12, 35],
        "XP": [35, 50]
    },
    "Dragon": {
        "Name": "Dragon",
        "HP": 100,
        "MAXHP": 100,
        "Attack": 8,
        "Gold": 100,
        "XP": [1000, 2000]
    },
}
