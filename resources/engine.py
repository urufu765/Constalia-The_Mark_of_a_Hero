"""
Any "graphical" rendering and processing is done here!
Do NOT stuff text only stuff here, that's for the text module.
Formally known as graphics.py for versions prior to 0.5
"""
from typing import List, Dict, Optional, Tuple
from resources.global_dic import pygame_variables as V
from resources.global_dic import variables as DV
from resources.global_dic import map_to_values as MD
from resources.global_dic import TEXTURE_FILES as TF
from resources.global_dic import test_color_dic_2 as CD
from resources.global_dic import version as VER
from resources.char import Player as p
from resources import jukebox as JB
from resources import char
from assets import quests
import pygame
from resources import mapper

# Debugger
Nyafim = False


class Engineer:
    # window
    size: Tuple[int, int]
    width: int
    height: int
    screen: Optional[pygame.Surface]
    w_tiles: int
    l_tiles: int
    tiles_number: Tuple[int, int]
    background: Optional[pygame.Surface]

    __characters: List[char.Characters]
    __run_stat: bool
    __map_view: List[List[any]]  # Will convert to List[str] later
    __text_view: List[str]
    __maps: Dict[int, mapper.Maps]

    ''' Some demo stuff first try and stuff idk
    def __init__(self):
        pygame.init()
        self.width = 900  # Always maintain integer divisibility with mrsw
        self.height = 600
        self.mrsw = 15  # Odd numbers only!
        self.mrsh = 7  # Odd numbers only!
        self.tiles = self.width / self.mrsw
        self.crsh = self.height - self.mrsh * self.tiles
        self.map_view = []
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption(
            f"Constalia: The Mark of a Hero [{V['specific']}]")
        for y in range(self.mrsh):
            for x in range(self.mrsw):
                self.map_view.append(
                    pygame.Rect(
                        self.tiles * x,
                        self.crsh + self.tiles * y,
                        self.width,
                        self.height))
        self.text_view = pygame.Rect(0, 0, self.width, self.crsh)
    '''
    def __init__(self, running: bool):
        # Main window
        self.w_tiles, self.l_tiles = 15, 15  # always odd numbers
        self.tile_num = (self.w_tiles, self.l_tiles)
        self.width = self.w_tiles * V['tile_size']
        self.height = self.l_tiles * V['tile_size']
        self.size = (self.width, self.height)
        self.screen = None
        self.background = None
        self.__characters = []
        self.__run_stat = running
        self.__map_view = []
        self.__maps = {
            0: mapper.Mithavil(),
            1: mapper.Home(),
            2: mapper.Ravia_House()
        }
        # self.__map = M[DV['m_id']]()
        self.__text_view = []  # Separate window potentially

    def __crop_map(self) -> Tuple[int, int]:
        """
        Crops the map
        Also attempts to match the map's size so it's more visually
        pleasing.
        Outputs offset: (y, x)
        """
        offset_y = DV['Y'] - (self.l_tiles - 1) // 2
        offset_x = DV['X'] - (self.w_tiles - 1) // 2
        # m = mapz[DV['m_id']].grid
        m = self.__maps[DV['m_id']]

        # y boundary checks
        if self.l_tiles >= m.map_y + 5:
            offset_y = 0 - ((self.l_tiles - m.map_y + 5) // 2)
        else:
            if offset_y < - 2:
                offset_y = - 2
            elif self.l_tiles + offset_y > m.map_y + 3:
                offset_y = m.map_y + 3 - self.l_tiles

        # x boundary checks
        if self.w_tiles >= m.map_x + 5:
            offset_x = 0 - ((self.w_tiles - m.map_x + 5) // 2)
        else:
            if offset_x < - 2:
                offset_x = - 2
            elif self.w_tiles + offset_x > m.map_x + 3:
                offset_x = m.map_x + 3 - self.w_tiles

        # cropping bit
        self.__map_view = []
        for y in range(offset_y, offset_y + self.l_tiles):
            temp = []
            for x in range(offset_x, offset_x + self.w_tiles):
                try:
                    if x == DV['X'] and y == DV['Y']:
                        temp.append('p')  # player
                    elif x < 0 or y < 0:
                        temp.append('o')
                    else:
                        temp.append(MD[m.grid[y][x]][0])
                except IndexError:
                    temp.append('o')  # out of bounds
                except KeyError:
                    temp.append(m.grid[y][x])
            self.__map_view.append(temp)
        return offset_y, offset_x

    def draw_main(self) -> None:
        """
        Draws the screen using the cropped map
        """
        offset = self.__crop_map()  # offset unused here for now
        # color mode
        for y, row in enumerate(self.__map_view):
            for x, block in enumerate(row):
                if len(TF[block]) == 1:
                    self.screen.blit(
                        pygame.image.load(TF[block][0]).convert_alpha(),
                        pygame.Rect(
                            x * V['tile_size'],
                            y * V['tile_size'],
                            V['tile_size'], V['tile_size']
                        ))
                # elif len(TF[block]) > 1:  (for multi-texture stuff)
                else:
                    self.screen.fill(
                        CD[block],
                        pygame.Rect(
                            x * V['tile_size'],
                            y * V['tile_size'],
                            V['tile_size'], V['tile_size']
                        ))
        pygame.display.flip()

    def get_value(self, y: int, x: int) -> str:
        """
        Returns the string at the specific coordinate
        """
        return self.__maps[DV['m_id']].grid[y][x]

    def new_game(self) -> None:
        """
        Initializes the game
        """
        pygame.display.set_caption(
            f"Constalia: The Mark of a Hero [{VER['detailed']}]")
        self.screen = pygame.display.set_mode(self.size)
        JB.jam(self.__maps[DV['m_id']].soundtrack)
        # self.background = pygame.image.load()  # note to self place this
        # in draw_main()
        # Insert initializing objects here


def battle_graphics_engine(map: int, position: List[int]) -> None:
    """
    A separate graphics engine made for battle. Just a little entry point
    once I get to the point of coding the battle sequence in.
    This is mostly just for reminding me though.
    """
    pass


def legacy_quest_output() -> None:
    """
    Prints the list of quests that are active.
    """
    box_of_texts = quests.check_quest()
    if Nyafim:
        print(box_of_texts)
    the_toggle = True
    if box_of_texts[0][0] == 'No active quests':
        the_toggle = False
    print(
        "┏Current━Quest:━━━━━━━━━━━┑"
        f"\n┃ {box_of_texts[0][0]}"
    )
    if the_toggle:
        print("┠Description:────────────")
        for thing in box_of_texts[0][1]:
            print(f"┃ {thing}")
        print(
            "┠Current─Objective:──────"
            f"\n┃ {box_of_texts[0][2]}"
        )
    print(
        "┣━━━━━━━━━━━━━━━━━━━━━━━━━┙"
        "\n┞Incomplete─Quests:───"
    )
    if len(box_of_texts[1]) == 0:
        print("│ No incomplete quests")
    else:
        for another_thing in box_of_texts[1]:
            print(f"│ {another_thing}")
    print("└─────────────────────")


def controls_output(controls: Dict[str, object]) -> None:
    """
    Prints the list of controls. Currently implemented in the main module,
    planning on moving it here.
    """
    pass


if __name__ == '__main__':  # For testing purposes
    import doctest
    doctest.testmod(verbose=True)
