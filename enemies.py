"""Contains the various enemies and their statistics"""
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
        self.gold = enemy_stats[enemy]['Gold']


enemy_stats = {
    "Goblin": {
        "Name": "Orc",
        "HP": 15,
        "MAXHP": 15,
        "Attack": 2,
        "Gold": 8
    },
    "Orc": {
        "Name": "Orc",
        "HP": 35,
        "MAXHP": 35,
        "Attack": 5,
        "Gold": 18
    },
    "Slime": {
        "Name": "Slime",
        "HP": 30,
        "MAXHP": 30,
        "Attack": 2,
        "Gold": 12
    },
    "Dragon": {
        "Name": "Dragon",
        "HP": 100,
        "MAXHP": 100,
        "Attack": 8,
        "Gold": 100
    },
}
