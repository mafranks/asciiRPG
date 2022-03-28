"""Maps for the player to navigate"""

map1 = [
    # x = 0    x = 1        x = 2      x = 3     x = 4     x = 5         x = 6
    [{"type": "PLAINS    ", "visible": True}, {"type": "PLAINS    ", "visible": False}, {"type": "PLAINS    ", "visible": False},  {"type": "PLAINS    ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "MOUNTAIN  ", "visible": False}, {"type": "CAVE      ", "visible": False}],  # y = 0
    [{"type": "FOREST    ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "HILLS     ", "visible": False}, {"type": "MOUNTAIN  ", "visible": False}],  # y = 1
    [{"type": "FOREST    ", "visible": False}, {"type": "FIELDS    ", "visible": False}, {"type": "BRIDGE    ", "visible": False}, {"type": "PLAINS    ", "visible": False}, {"type": "HILLS     ", "visible": False}, {"type": "FOREST    ", "visible": False}, {"type": "HILLS     ", "visible": False}],  # y = 2
    [{"type": "PLAINS    ", "visible": False}, {"type": "ITEM_SHOP ", "visible": False}, {"type": "TOWN      ", "visible": False}, {"type": "MAYOR     ", "visible": False}, {"type": "PLAINS    ", "visible": False}, {"type": "HILLS     ", "visible": False}, {"type": "MOUNTAIN  ", "visible": False}],  # y = 3
    [{"type": "PLAINS    ", "visible": False}, {"type": "FIELDS    ", "visible": False}, {"type": "FIELDS    ", "visible": False}, {"type": "PLAINS    ", "visible": False}, {"type": "HILLS     ", "visible": False}, {"type": "MAGIC_SHOP", "visible": False}, {"type": "MOUNTAIN  ", "visible": False}]   # y = 4
]

biomes = {
    "PLAINS    ": {
        "text": "PLAINS",
        "enemies": True
    },
    "FOREST    ": {
        "text": "FOREST",
        "enemies": True
    },
    "FIELDS    ": {
        "text": "FIELDS",
        "enemies": False
    },
    "BRIDGE    ": {
        "text": "BRIDGE",
        "enemies": True
    },
    "TOWN      ": {
        "text": "TOWN",
        "enemies": False
    },
    "ITEM_SHOP ": {
        "text": "ITEM SHOP",
        "enemies": False
    },
    "MAGIC_SHOP": {
        "text": "MAGIC SHOP",
        "enemies": False
    },
    "MAYOR     ": {
        "text": "MAYOR",
        "enemies": False
    },
    "CAVE      ": {
        "text": "CAVE",
        "enemies": False
    },
    "MOUNTAIN  ": {
        "text": "MOUNTAIN",
        "enemies": True
    },
    "HILLS     ": {
        "text": "HILLS",
        "enemies": True
    },
}