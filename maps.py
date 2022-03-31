"""Maps for the player to navigate"""

starting_map = [
                    # x = 0                             x = 1                                 x = 2                                    x = 3                              x = 4                                 x = 5                                       x = 6
    [{"type": "plains", "visible": True}, {"type": "plains", "visible": False}, {"type": "plains", "visible": False},  {"type": "plains", "visible": False}, {"type": "forest", "visible": False}, {"type": "mountain", "visible": False}, {"type": "cave", "visible": False}],      # y = 0
    [{"type": "forest", "visible": False}, {"type": "forest", "visible": False}, {"type": "forest", "visible": False}, {"type": "forest", "visible": False}, {"type": "forest", "visible": False}, {"type": "hills", "visible": False}, {"type": "mountain", "visible": False}],     # y = 1
    [{"type": "forest", "visible": False}, {"type": "fields", "visible": False}, {"type": "bridge", "visible": False}, {"type": "plains", "visible": False}, {"type": "hills", "visible": False}, {"type": "forest", "visible": False}, {"type": "hills", "visible": False}],       # y = 2
    [{"type": "plains", "visible": False}, {"type": "item_shop", "visible": False}, {"type": "town", "visible": False}, {"type": "plains", "visible": False}, {"type": "plains", "visible": False}, {"type": "hills", "visible": False}, {"type": "mountain", "visible": False}],    # y = 3
    [{"type": "plains", "visible": False}, {"type": "fields", "visible": False}, {"type": "fields", "visible": False}, {"type": "plains", "visible": False}, {"type": "hills", "visible": False}, {"type": "magic_shop", "visible": False}, {"type": "mountain", "visible": False}]  # y = 4
]

town_map = [
                # x = 0                             x = 1
    [{"type": "entrance", "visible": True}, {"type": "sidewalk", "visible": False}],      # y = 0
    [{"type": "inn", "visible": False}, {"type": "item_shop", "visible": False}],         # y = 1
    [{"type": "town_hall", "visible": False}, {"type": "magic_shop", "visible": False}],  # y = 2
]

biomes = {
    "plains": {
        "text": "PLAINS",
        "display": "  PLAINS  ",
        "enemies": True
    },
    "forest": {
        "text": "FOREST",
        "display": "  FOREST  ",
        "enemies": True
    },
    "fields": {
        "text": "FIELDS",
        "display": "  FIELDS  ",
        "enemies": False
    },
    "bridge": {
        "text": "BRIDGE",
        "display": "  BRIDGE  ",
        "enemies": True
    },
    "town": {
        "text": "TOWN",
        "display": "   TOWN   ",
        "enemies": False
    },
    "item_shop": {
        "text": "ITEM SHOP",
        "display": " ITEM_SHOP",
        "enemies": False
    },
    "magic_shop": {
        "text": "MAGIC SHOP",
        "display": "MAGIC_SHOP",
        "enemies": False
    },
    "town_hall": {
        "text": "TOWN_HALL",
        "display": " TOWN HALL ",
        "enemies": False
    },
    "cave": {
        "text": "CAVE",
        "display": "   CAVE   ",
        "enemies": False
    },
    "mountain": {
        "text": "MOUNTAIN",
        "display": " MOUNTAIN ",
        "enemies": True
    },
    "hills": {
        "text": "HILLS",
        "display": "  HILLS   ",
        "enemies": True
    },
    "inn": {
        "text": "INN",
        "display": "   INN    ",
        "enemies": False
    },
    "entrance": {
        "text": "ENTRANCE",
        "display": " ENTRANCE ",
        "enemies": False
    },
    "sidewalk": {
        "text": "SIDEWALK",
        "display": " SIDEWALK ",
        "enemies": False
    }
}