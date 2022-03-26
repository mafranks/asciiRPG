"""Maps for the player to navigate"""

map1 = [
    # x = 0    x = 1        x = 2      x = 3     x = 4     x = 5         x = 6
    ["plains", "plains",    "plains",  "plains", "forest", "mountain",   "cave"],      # y = 0
    ["forest", "forest",    "forest",  "forest", "forest", "hills",      "mountain"],  # y = 1
    ["forest", "fields",    "bridge",  "plains", "hills",  "forest",     "hills"],     # y = 2
    ["plains", "item_shop", "town",    "mayor",  "plains", "hills",      "mountain"],  # y = 3
    ["plains", "fields",    "fields",  "plains", "hills",  "magic_shop", "mountain"]   # y = 4
]

biomes = {
    "plains": {
        "text": "PLAINS",
        "enemies": True
    },
    "forest": {
        "text": "FOREST",
        "enemies": True
    },
    "fields": {
        "text": "FIELDS",
        "enemies": False
    },
    "bridge": {
        "text": "BRIDGE",
        "enemies": True
    },
    "town": {
        "text": "TOWN",
        "enemies": False
    },
    "item_shop": {
        "text": "ITEM SHOP",
        "enemies": False
    },
    "magic_shop": {
        "text": "MAGIC SHOP",
        "enemies": False
    },
    "mayor": {
        "text": "MAYOR",
        "enemies": False
    },
    "cave": {
        "text": "CAVE",
        "enemies": False
    },
    "mountain": {
        "text": "MOUNTAIN",
        "enemies": True
    },
    "hills": {
        "text": "HILLS",
        "enemies": True
    },
}