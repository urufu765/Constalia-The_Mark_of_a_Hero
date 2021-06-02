"""
An upgrade to maps.py that doesn't use hard coded maps.
"""
from typing import Dict, List
from resources.global_dic import LOOP_FILES as LF
from resources.global_dic import map_to_values as MD


class Maps:
    map_id: int
    map_name: str
    map_x: int
    map_y: int
    background: str
    soundtrack: str
    __map_stuff: Dict[str, List[List[int]]]
    grid: List[List[str]]
    # Mapstuff Dict[id, list(list(y, x, y+, x+))]

    def __init__(
        self, map_id: int, map_name: str, map_y: int, map_x: int,
        map_stuff: Dict[str, List[List[int]]],
        background='', soundtrack=LF[0]
            ) -> None:
        self.map_id = map_id
        self.map_name = map_name
        self.map_x = map_x
        self.map_y = map_y
        self.background = background
        self.soundtrack = soundtrack
        self.__map_stuff = map_stuff
        self.grid = self.load_map()

    def load_map(self) -> List[List[str]]:
        """
        Makes a map using __map_stuff and placing it into grid
        This is to use RAM instead of CPU when displaying since the CPU is
        used less if the whole map is loaded in the beginning instead of
        drawing the map every tick.

        There's probably a more efficient way of doing this (currently this
        is O[n^4] or something) but at the moment this is the least complex
        so...
        """
        temp = []
        # Making a box
        for y in range(self.map_y + 1):
            '''
            temp = []
            for x in range(self.map_x):
                temp.append('0')
            self.grid.append(temp)
            '''
            temp.append(['0' for i in range(self.map_x + 1)])

        # 'draws' each thing
        for key in self.__map_stuff:
            if MD[key][1]:  # Checks if visible or not
                for obj in self.__map_stuff[key]:  # 'drawing' part
                    if len(obj) == 0:
                        continue  # using this for less nested blocks
                    for y in range(obj[2] + 1):
                        for x in range(obj[3] + 1):
                            temp[obj[0] + y][obj[1] + x] = key
        return temp

    # TODO: find a way to not use hard coding for __map_stuff


class Mithavil(Maps):
    """
    This is a biggun.

    Map of Mithavil (scrapped the idea of having north and south)
    Reminder to self: Exits/doors that are on the sides and top need
    "front steps" for visual purposes, while those that are on the bottom
    can get away with replacing part of the wall

    Also consult the onenote docs for the visual representation of the map
    """
    def __init__(self) -> None:
        """
        Initializes Mithavil map

        Notes:
        Wall should always be the first item. Check with other
        python versions to check if ordering will cause a problem
        or not... if so then make a compensating code in the drawing bit
        Also tree = wall
        """
        super().__init__(
            0, "Mithavil", 30, 57, {
                'grass': [
                    [0, 0, 30, 57]
                ],
                # Generics
                'tree': [
                    [0, 0, 0, 57],
                    [1, 0, 29, 0],
                    [1, 57, 29, 0],
                    [30, 44, 0, 12]
                    ],
                'house': [  # TODO: maybe split this up into house and roof
                    # Left
                    [16, 4, 5, 5],  # Mayor's house TODO: fix visual repr
                    [16, 11, 2, 4],
                    [7, 14, 3, 4],
                    [18, 17, 3, 3],
                    [15, 23, 5, 4],
                    [22, 25, 2, 4],
                    [13, 32, 3, 2],
                    [6, 35, 3, 2],
                    [17, 38, 2, 4],
                    [13, 39, 2, 4],
                    [24, 41, 2, 3],
                    [3, 45, 5, 3],  # Home
                    [15, 45, 3, 3],
                    [23, 48, 3, 2],
                    [8, 51, 4, 4],
                    [19, 53, 4, 2]  # Ravia's house
                    # Right
                    ],  # TODO: and maybe have different house variants
                'path': [
                    []  # TODO: both in code and visual representation
                ],
                'ocean': [
                    [29, 1, 1, 2],
                    [28, 4, 2, 5],
                    [27, 10, 3, 4],
                    [26, 15, 4, 19],
                    [27, 35, 3, 3],
                    [28, 39, 2, 3],
                    [29, 43, 1, 0]
                ],
                'river': [
                    [0, 41, 3, 0],
                    [2, 40, 7, 0],
                    [9, 39, 2, 0],
                    [10, 38, 2, 0],
                    [12, 37, 3, 0],
                    [14, 36, 5, 0],
                    [18, 35, 3, 0],
                    [20, 34, 3, 0],
                    [23, 33, 2, 0],
                    [24, 32, 1, 0]
                ],
                # Exits (departure) (fix in visual representation)
                'west exit': [[12, 0, 1, 0]],
                'east exit': [[15, 57, 1, 0]],
                # Entrances (to homes)
                'home gate': [[8, 46, 0, 0]],
                'ravia gate': [[20, 52, 0, 0]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # 'mith ': [[]],
                # Signs/directions (TODO)

                # Others
                'farm': [[3, 42, 5, 2]],
                'town hall': [[3, 4, 7, 7]],
                'market': [[2, 22, 7, 7]],  # TODO: make this less square
                'bridge': [
                    [11, 37, 1, 2],
                    [21, 34, 1, 1]
                ]
            }, soundtrack=LF['mithavil'])


class Home(Maps):
    """visual
        000000000011
        012345678901
        XXXXXXXXXXXX 00
        XBB   XXXXXX 01
        X     XXXXXX 02
        XXDXXXX   BX 03
        X     X f BX 04
        X     D    X 05
        X     XXXXXX 06
        X          X 07
        X  TTTC    X 08
        X  TTT     X 19
        X      C   X 10
        XXXXXXXXXEXX 11

    # TODO: redo place
    """
    def __init__(self) -> None:
        """
        Initializes home map

        Notes:
        Hardcoded wall that accounts for other objects
        Reminder to self: Don't do this, it's not like I'm appending
        the values to the map. I'm replacing existing 'tiles'
        Don't do this unless it really harms performance like if
        I were to draw the entire map as a single wall than hollow it
        out... don't do the hollow out thing, it's tempting as a lazy
        developer, but don't you dare do it.
        """
        super().__init__(
            1, "Home", 11, 11, {
                'floor_wood': [
                    [0, 0, 11, 11]
                ],
                'wall': [
                    [0, 0, 11, 0],
                    [0, 1, 0, 10],
                    [1, 6, 1, 5],
                    [3, 1, 0, 0],
                    [3, 3, 0, 3],
                    [4, 6, 0, 0],
                    [3, 11, 8, 0],
                    [6, 6, 0, 4],
                    [11, 1, 0, 7],
                    [11, 10, 0, 0]],
                # TODO: don't hardcode characters in map
                'rubi': [[8, 5, 0, 0]],
                'john': [[10, 7, 0, 0]],
                'home_table': [[8, 2, 1, 2]],
                'firay_bed': [[3, 10, 1, 0]],
                'rubi_bed': [[1, 1, 0, 1]],
                'home gate': [[11, 9, 0, 0]],
                'rubi_door': [[3, 2, 0, 0]],
                'firay_door': [[5, 6, 0, 0]]
            }, soundtrack=LF['home'])


class Ravia_House(Maps):
    """visual
        0000000000111
        0123456789012
        XXXXXXXXXXXXX 00
        XBB        TX 01
        X          TX 02
        XXXXDXXXXXXXX 03
        E           X 04
        X     C     X 05
        X   TTTT    X 06
        X   TTTT    X 07
        X   TTTT    X 08
        X           X 09
        X           X 10
        XXXXXXXXXXXXX 11

    # TODO: Perhaps add chests and stuff
    Actually, redo place
    """
    def __init__(self) -> None:
        """
        Initializes Ravia's home
        """
        super().__init__(
            2, "Ravia's House", 11, 12, {
                # TODO: Check with other python versions for dict ordering
                'floor_wood': [
                    [0, 0, 11, 12]
                ],
                'wall': [
                    [0, 0, 0, 12],
                    [1, 0, 10, 0],
                    [3, 1, 0, 10],
                    [11, 1, 0, 11],
                    [1, 12, 9, 0]],
                'ravia': [[5, 6, 0, 0]],
                'ravia table': [[6, 4, 2, 3]],
                'ravia desk': [[1, 11, 1, 0]],
                'ravia bed': [[1, 1, 0, 1]],
                'ravia gate': [[4, 0, 0, 0]],
                'ravia door': [[3, 4, 0, 0]],
            }, soundtrack=LF['ravia'])


