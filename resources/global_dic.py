"""
Contains everything regarding variables
"""
from assets import maps as m
from resources.char import Player as p

# Note to self: DON'T FORGET TO UPDATE THIS YOU FORGETFUL IDIOT!
# Also never call these versions directly, they're for internal use only
v_long = 'Version 0'
v_short = '0'
v_major = '5'
v_minor = '0'
v_hotfx = '0'
v_stype = 'n'  # u = untested, t = tested, r = release(able), n = N/A
v_ltype = 'N/A'

# Version
version = {
    'common': f'v {v_short}.{v_major}.{v_minor}',
    'specific': f'v {v_short}.{v_major}.{v_minor}.{v_hotfx}',
    'detailed': f'v {v_short}.{v_major}.{v_minor}.{v_hotfx}{v_stype}',
    'fancy': f'{v_long} ({v_short}.{v_major}.{v_minor}.{v_hotfx})[{v_ltype}]'
}

# Global dictionary!
variables = {
    'Y': 5,
    'X': 9,
    'm_id': 1,
    'stamina': 20
    }

# Collision codes
solids = {
    'Mithavil': [2, 3, 5, 6, 7, 8, 9],
    'Mithavil Interior': [1, 2, 3, 4, 5, 8, 9]
    }

# Map class lookup table
map_class = {
    0: m.Mithavil,
    1: m.Home,
    2: m.Raviahouse
    }

# Generating graphics(legacy)
legacy_visuals = {
    'outtaboundz': "▒",
    'Mithavil': [' ', '҈', '■', '⌠', '▓', 'ﬕ', '‼', '□', 'Ξ', '█'],
    'Mithavil Interior': ['░', 'C', '▒', '╬', '┃', '━', '│', '─', 'Ξ', '█']
    }

visuals = {
    'tile_size': 50,
}

test_color_dic = {  # for testing only
    'p': (255, 0, 0),  # player
    0: (110, 110, 110),
    1: (0, 255, 0),
    8: (255, 180, 180),
    2: (0, 0, 255),
    3: (0, 0, 255),
    4: (90, 90, 255),
    5: (90, 90, 255),
    6: (90, 90, 255),
    7: (90, 90, 255),
    9: (70, 70, 70),
    'w': (255, 255, 255),  # white
    'o': (0, 0, 0),  # outtaboundz
}

# Every single door in the game that's noteworthy
doors = {
    # 'Map ID-Y-X': [Door ID, Door locked check, Map class, Y, X]
    # Mithavil doors
    '0-5-12': ['0_home', False, 1, 10, 10],
    '0-17-10': ['0_ravia', False, 2, 9, 2],
    '0-4-24': ['0_NA', True, 0, 4, 25],
    '0-17-6': ['0_NA', True, 0, 17, 7],
    '0-20-6': ['0_NA', True, 0, 20, 7],
    '0-19-10': ['0_NA', True, 0, 19, 9],
    '0-16-26': ['0_NA', True, 0, 16, 25],
    '0-25-22': ['0_hall', True, 0, 25, 21],
    '0-7-2': ['0_exit_forest', True, 0, 7, 3],
    '0-32-12': ['0_exit_market', True, 0, 31, 12],
    # Home doors
    '1-11-10': ['1_exit', False, 0, 6, 12],
    # Ravia's house doors
    '2-10-2': ['2_exit', False, 0, 17, 9],
    '2-4-5': ['2_bedroom', True, 2, 5, 5]
}

# Every single interactable that can be seen in the game
interactables = {
    # 'Map ID-Y-X': [Interactable ID, Type, Trigger]
    # Mithavil(0)
    # Sign(News)
    '0-26-12': ['mith_locan_news', 'sign', False],
    # Sign 2(direction)
    '0-30-13': ['mith_direction', 'sign', False],
    '0-30-14': ['mith_direction', 'sign', False],
    # Home(1)
    # Firay's bed
    '1-4-11': ['firay_bed', 'bed', True],
    '1-5-11': ['firay_bed', 'bed', True],
    # Rubi's bed
    '1-2-2': ['rubi_bed', 'bed', False],
    '1-2-3': ['rubi_bed', 'bed', False],
    # Table
    '1-9-4': ['home_table', 'table', False],
    '1-9-5': ['home_table', 'table', False],
    '1-9-6': ['home_table', 'table', False],
    '1-10-4': ['home_table', 'table', False],
    '1-10-5': ['home_table', 'table', False],
    '1-10-6': ['home_table', 'table', False],
    # Characters
    '1-9-7': ['rubi', 'npc', True],
    '1-11-8': ['john', 'ally', False],
    # Ravia's house(2)
    # Table
    '2-7-5': ['ravia_table', 'table', False],
    '2-7-6': ['ravia_table', 'table', False],
    '2-7-7': ['ravia_table', 'table', False],
    '2-7-8': ['ravia_table', 'table', False],
    '2-8-5': ['ravia_table', 'table', False],
    '2-8-8': ['ravia_table', 'table', False],
    '2-9-5': ['ravia_table', 'table', False],
    '2-9-6': ['ravia_table', 'table', False],
    '2-9-7': ['ravia_table', 'table', False],
    '2-9-8': ['ravia_table', 'table', False],
    # Desk
    '2-2-12': ['ravia_desk', 'table', False],
    '2-3-12': ['ravia_desk', 'table', False],
    # Characters
    '2-6-7': ['ravia', 'npc', False]
}

# Quests, for loading saves and stuff
quests = {
    # [step, status, [other assets for quest(string ONLY!)]]
    'get_leaf': [0, 'Inactive', ['n', 'n']]
}


# control schemes
class controls:
    # Use null as a template
    control_null = {
        'Up': [],
        'Down': [],
        'Left': [],
        'Right': [],
        'Quest': [],
        'Inventory': [],
        'Save': ["Z", "z"],
        'Load': ["X", "x"],
        'Quit': ["P", "p"]
    }

    # For the general public
    control_wasd = {
        'Up': ["W", "w"],
        'Down': ["S", "s"],
        'Left': ["A", "a"],
        'Right': ["D", "d"],
        'Quest': ["Q", "q"],
        'Inventory': ["E", "e"],
        'Save': ["Z", "z"],
        'Load': ["X", "x"],
        'Quit': ["P", "p"]
    }

    # For those who want it
    control_nesw = {
        'Up': ["N", "n"],
        'Down': ["S", "s"],
        'Left': ["W", "w"],
        'Right': ["E", "e"],
        'Quest': ["Q", "q"],
        'Inventory': ["I", "i"],
        'Save': ["Z", "z"],
        'Load': ["X", "x"],
        'Quit': ["P", "p"]
    }

    # For those who want to use this
    control_nump = {
        'Up': ["8"],
        'Down': ["2", "5"],
        'Left': ["4"],
        'Right': ["6"],
        'Quest': ["7"],
        'Inventory': ["9"],
        'Save': ["+"],
        'Load': ["-"],
        'Quit': ["*"]
    }

    # For the questionable
    control_udlr = {
        'Up': ["U", "u"],
        'Down': ["D", "d"],
        'Left': ["L", "l"],
        'Right': ["R", "r"],
        'Quest': ["Q", "q"],
        'Inventory': ["I", "i"],
        'Save': ["Z", "z"],
        'Load': ["X", "x"],
        'Quit': ["P", "p"]
    }

    # Lookup table
    control_schemes = {
        1: control_nesw,
        2: control_udlr,
        3: control_wasd,
        4: control_nump
    }
