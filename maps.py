"""Maps for the player to navigate"""

starting_map = [
    [{"type": "plains", "visible": True}, {"type": "plains", "visible": False},
     {"type": "plains", "visible": False}, {"type": "plains", "visible": False},
     {"type": "forest", "visible": False}, {"type": "mountain", "visible": False},
     {"type": "cave", "visible": False}],

    [{"type": "forest", "visible": False}, {"type": "forest", "visible": False},
     {"type": "forest", "visible": False}, {"type": "forest", "visible": False},
     {"type": "forest", "visible": False}, {"type": "hills", "visible": False},
     {"type": "mountain", "visible": False}],

    [{"type": "forest", "visible": False}, {"type": "fields", "visible": False},
     {"type": "bridge", "visible": False}, {"type": "plains", "visible": False},
     {"type": "hills", "visible": False}, {"type": "forest", "visible": False},
     {"type": "hills", "visible": False}],

    [{"type": "plains", "visible": False}, {"type": "item_shop", "visible": False},
     {"type": "town", "visible": False}, {"type": "castle", "visible": False},
     {"type": "plains", "visible": False}, {"type": "hills", "visible": False},
     {"type": "mountain", "visible": False}],

    [{"type": "plains", "visible": False}, {"type": "fields", "visible": False},
     {"type": "fields", "visible": False}, {"type": "plains", "visible": False},
     {"type": "hills", "visible": False}, {"type": "magic_shop", "visible": False},
     {"type": "mountain", "visible": False}]
]

town_map = [
    [{"type": "entrance", "visible": True}, {"type": "sidewalk", "visible": False},
     {"type": "sidewalk", "visible": False}, {"type": "sidewalk", "visible": False},
     {"type": "sidewalk", "visible": False}, {"type": "sidewalk", "visible": False},
     {"type": "clayton", "visible": False}],

    [{"type": "sidewalk", "visible": False}, {"type": "sidewalk", "visible": False},
     {"type": "sidewalk", "visible": False}, {"type": "inn", "visible": False},
     {"type": "sidewalk", "visible": False}, {"type": "item_shop", "visible": False},
     {"type": "sidewalk", "visible": False}],

    [{"type": "sidewalk", "visible": False}, {"type": "town_hall", "visible": False},
     {"type": "sidewalk", "visible": False}, {"type": "sidewalk", "visible": False},
     {"type": "magic_shop", "visible": False}, {"type": "sidewalk", "visible": False},
     {"type": "sidewalk", "visible": False}]
]

cave_map = [
    [{"type": "entrance", "visible": True}, {"type": "stone", "visible": False}, {"type": "water", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "water", "visible": False},
     {"type": "chest", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "dirt", "visible": False}, {"type": "stone", "visible": False}, {"type": "water", "visible": False},
     {"type": "stone", "visible": False}],

    [{"type": "water", "visible": False}, {"type": "stone", "visible": False}, {"type": "dirt", "visible": False},
     {"type": "stone", "visible": False}, {"type": "water", "visible": False}, {"type": "stone", "visible": False},
     {"type": "water", "visible": False}],

    [{"type": "water", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "water", "visible": False}, {"type": "stone", "visible": False}, {"type": "dirt", "visible": False},
     {"type": "water", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "water", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "dirt", "visible": False}, {"type": "water", "visible": False},
     {"type": "chest_spc", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "dirt", "visible": False}, {"type": "stone", "visible": False},
     {"type": "water", "visible": False}, {"type": "water", "visible": False}, {"type": "chest", "visible": False},
     {"type": "dirt", "visible": False}]
]

castle_map = [
    [{"type": "entrance", "visible": True}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "chest", "visible": False},
     {"type": "stone", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "tower_door", "visible": False}, {"type": "stone", "visible": False},
     {"type": "chest_spc", "visible": False}],

    [{"type": "stone", "visible": False}, {"type": "chest", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}, {"type": "stone", "visible": False}, {"type": "stone", "visible": False},
     {"type": "stone", "visible": False}]
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
    "castle": {
        "text": "CASTLE",
        "display": "  CASTLE  ",
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
    "sidewalk": {
        "text": "SIDEWALK",
        "display": " SIDEWALK ",
        "enemies": False
    },
    "entrance": {
        "text": "ENTRANCE",
        "display": " ENTRANCE ",
        "enemies": False
    },
    "stone": {
        "text": "STONE",
        "display": "  STONE   ",
        "enemies": True
    },
    "dirt": {
        "text": "DIRT",
        "display": "   DIRT   ",
        "enemies": True
    },
    "water": {
        "text": "WATER",
        "display": "  WATER   ",
        "enemies": True
    },
    "chest": {
        "text": "CHEST",
        "display": "  CHEST   ",
        "enemies": False
    },
    "chest_spc": {
        "text": "CHEST",
        "display": "  CHEST   ",
        "enemies": False
    },
    "clayton": {
        "text": "CLAYTON",
        "display": " CLAYTON  ",
        "enemies": False
    },
    "tower_door": {
        "text": "TOWER DOOR",
        "display": "TOWER DOOR",
        "enemies": False
    }
}
