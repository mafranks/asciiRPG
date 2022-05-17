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
        "Immunity": [],
        "Weak": []
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
        "Immunity": [],
        "Weak": []
    },
    "Wolf": {
        "Name": "Wolf",
        "MAXHP": 20,
        "Attack": 8,
        "Gold": [5, 10],
        "XP": 24,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Crazy Horse": {
        "Name": "Crazy Horse",
        "MAXHP": 64,
        "Attack": 10,
        "Gold": [10, 20],
        "XP": 63,
        "Terrain": ['plains', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Skeleton": {
        "Name": "Skeleton",
        "MAXHP": 10,
        "Attack": 10,
        "Gold": [1, 6],
        "XP": 9,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2],
        "Resistance": ['ice'],
        "Immunity": [],
        "Weak": ['fire', 'fire2']
    },
    "Black Widow": {
        "Name": "Black Widow",
        "MAXHP": 28,
        "Attack": 10,
        "Gold": [8, 20],
        "XP": 30,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Gigas Worm": {
        "Name": "Gigas Worm",
        "MAXHP": 56,
        "Attack": 17,
        "Gold": [10, 20],
        "XP": 63,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": ['fire', 'fire2']
    },
    "Warg Wolf": {
        "Name": "Warg Wolf",
        "MAXHP": 72,
        "Attack": 14,
        "Gold": [17, 25],
        "XP": 93,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Werewolf": {
        "Name": "Werewolf",
        "MAXHP": 68,
        "Attack": 14,
        "Gold": [62, 72],
        "XP": 135,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Zombie": {
        "Name": "Zombie",
        "MAXHP": 20,
        "Attack": 10,
        "Gold": [8, 16],
        "XP": 24,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['ice', 'ice2'],
        "Immunity": [],
        "Weak": ['fire', 'firew']
    },
    "Ghoul": {
        "Name": "Ghoul",
        "MAXHP": 48,
        "Attack": 8,
        "Gold": [45, 55],
        "XP": 93,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['ice', 'ice2'],
        "Immunity": [],
        "Weak": ['fire', 'fire2']
    },
    "Garland": {
        "Name": "Garland",
        "MAXHP": 212,
        "Attack": 15,
        "Gold": [240, 260],
        "XP": 130,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Cobra": {
        "Name": "Cobra",
        "MAXHP": 56,
        "Attack": 6,
        "Gold": [45, 55],
        "XP": 123,
        "Terrain": ['plains', 'fields', 'hills'],
        "Levels": [1, 2, 3],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Ogre": {
        "Name": "Ogre",
        "MAXHP": 100,
        "Attack": 18,
        "Gold": [190, 200],
        "XP": 195,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Ogre Chief": {
        "Name": "Ogre Chief",
        "MAXHP": 132,
        "Attack": 23,
        "Gold": [295, 305],
        "XP": 282,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Lizard": {
        "Name": "Lizard",
        "MAXHP": 92,
        "Attack": 18,
        "Gold": [45, 55],
        "XP": 153,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Pirate": {
        "Name": "Pirate",
        "MAXHP": 24,
        "Attack": 10,
        "Gold": [35, 45],
        "XP": 40,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Sahagin": {
        "Name": "Sahagin",
        "MAXHP": 28,
        "Attack": 10,
        "Gold": [25, 35],
        "XP": 30,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire', 'fire2'],
        "Immunity": [],
        "Weak": ['lightning', 'lightning2']
    },
    "Sahagin Chief": {
        "Name": "Sahagin Chief",
        "MAXHP": 64,
        "Attack": 15,
        "Gold": [100, 110],
        "XP": 105,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire', 'fire2'],
        "Immunity": [],
        "Weak": ['lighting', 'lightning2']
    },
    "Buccaneer": {
        "Name": "Buccaneer",
        "MAXHP": 50,
        "Attack": 14,
        "Gold": [110, 130],
        "XP": 60,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
    },
    "Shark": {
        "Name": "Shark",
        "MAXHP": 120,
        "Attack": 22,
        "Gold": [60, 70],
        "XP": 267,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire', 'fire2'],
        "Immunity": [],
        "Weak": ['lightning', 'lightning2']
    },
    "Bigeyes": {
        "Name": "Bigeyes",
        "MAXHP": 10,
        "Attack": 4,
        "Gold": [5, 15],
        "XP": 42,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": ['fire'],
        "Immunity": [],
        "Weak": ['lighning', 'lightning2']
    },
    "Tarantula": {
        "Name": "Tarantula",
        "MAXHP": 64,
        "Attack": 5,
        "Gold": [40, 60],
        "XP": 141,
        "Terrain": ['plains', 'forest', 'fields', 'hills'],
        "Levels": [1, 2, 3, 4],
        "Resistance": [],
        "Immunity": [],
        "Weak": []
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
        "Immunity": ["fire", "fire2"],
        "Weak": []
    }
}

enemy_list = [enemy for enemy in enemy_stats]
