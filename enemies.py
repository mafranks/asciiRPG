"""Contains the various enemies and their statistics"""
import random


class Enemy:
    """Object containing all of the enemy data"""
    def __init__(self, enemy):
        self.name = enemy_stats[enemy]['Name']
        self.hp = enemy_stats[enemy]['MAXHP'],
        self.maxhp = enemy_stats[enemy]['MAXHP'],
        self.attack = enemy_stats[enemy]['Attack'],
        self.gold = random.randint(enemy_stats[enemy]['Gold'][0], enemy_stats[enemy]['Gold'][1])
        self.xp = enemy_stats[enemy]['XP']
        self.resistance = enemy_stats[enemy]['Resistance']
        self.immunity = enemy_stats[enemy]['Immunity']


"""
Enemy Parameters:
Name: Name
MAXHP: Maximum hit points
Attack: Physical attack power
Gold: Amount of gold to drop upon defeat
XP: Amount of xp the player gains upon defeat
Terrain: Terrain types the enemy will spawn on
Levels: Player level this enemy will spawn on
Resistance: Magic types or Physical attack the enemy is resistant to (reduces effect by 25%)
Immunity: Magic types or Physical attack the enemy is immune to (reduces effect by 100%)
"""
enemy_stats = {
    "Goblin": {
        "Name": "Goblin",
        "MAXHP": 8,
        "Attack": 4,
        "Gold": [5, 10],
        "XP": 6,
        "Terrain": ['plains', 'fields', 'hills'],
        "Levels": [1, 2, 3],
        "Resistance": ['fire'],
        "Immunity": []
    },
    "Goblin Guard": {
        "Name": "Goblin Guard",
        "MAXHP": 16,
        "Attack": 8,
        "Gold": [10, 15],
        "XP": 18,
        "Terrain": ['plains', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire2'],
        "Immunity": ['fire']
    },
    "Cobra": {
        "Name": "Cobra",
        "HP": 56,
        "MAXHP": 15,
        "Attack": 6,
        "Gold": [5, 30],
        "XP": 25,
        "Terrain": ['plains', 'fields', 'hills'],
        "Levels": [1, 2, 3],
        "Resistance": ['fire'],
        "Immunity": []
    },
    "Black Widow": {
        "Name": "Black Widow",
        "MAXHP": 28,
        "Attack": 10,
        "Gold": [8, 20],
        "XP": 30,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire'],
        "Immunity": []
    },
    "Wolf": {
        "Name": "Wolf",
        "MAXHP": 20,
        "Attack": 8,
        "Gold": [5, 10],
        "XP": 24,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire'],
        "Immunity": []
    },
    "Wizard": {
        "Name": "Wizard",
        "MAXHP": 500,
        "Attack": 8,
        "Gold": [100, 200],
        "XP": 1000,
        "Terrain": ['tower_door'],
        "Levels": [6, 7, 8, 9, 10],
        "Resistance": ["lightning", "lightning2"],
        "Immunity": ["fire", "fire2"]
    }
}

enemy_list = [enemy for enemy in enemy_stats]
