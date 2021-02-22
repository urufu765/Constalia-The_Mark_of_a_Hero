"""
Any "graphical" rendering and processing is done here!
Do NOT stuff text only stuff here, that's for the text module.
Formally known as graphics.py for versions prior to 0.5
"""
from typing import List, Dict, Optional, Tuple
from resources.global_dic import map_class as mapz
from resources.global_dic import legacy_visuals as visual_dic
from resources.global_dic import pygame_variables as V
from resources.global_dic import variables as DV
from resources.global_dic import test_color_dic as CD
from resources.global_dic import version as VER
from resources.char import Player as p
from resources import char
from assets import quests

# Debugger
Nyafim = False

try:
    import pygame

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

            self.__text_view = []  # Separate window potentially

        def __crop_map(self) -> Tuple[int, int]:
            """
            Crops the map from maps.py
            Also attempts to match the map's size so it's more visually
            pleasing.
            Outputs offset: (y, x)
            """
            offset_y = DV['Y'] - (self.l_tiles - 1) // 2
            offset_x = DV['X'] - (self.w_tiles - 1) // 2
            m = mapz[DV['m_id']].grid

            # y boundary checks
            if self.l_tiles >= len(m) + 4:
                offset_y = 0 - ((self.l_tiles - len(m) + 4) // 2)
            else:
                if offset_y < - 2:
                    offset_y = - 2
                elif self.l_tiles + offset_y > len(m) + 2:
                    offset_y = len(m) + 2 - self.l_tiles

            # x boundary checks
            if self.w_tiles >= len(m[0]) + 4:
                offset_x = 0 - ((self.w_tiles - len(m[0]) + 4) // 2)
            else:
                if offset_x < - 2:
                    offset_x = - 2
                elif self.w_tiles + offset_x > len(m[0]) + 2:
                    offset_x = len(m[0]) + 2 - self.w_tiles

            # cropping bit
            self.__map_view = []
            for y in range(offset_y, offset_y + self.l_tiles):
                temp = []
                for x in range(offset_x, offset_x + self.w_tiles):
                    try:
                        if x == DV['X'] and y == DV['Y']:
                            temp.append('p')  # player
                        else:
                            temp.append(m[y][x])
                    except IndexError:
                        temp.append('o')  # out of bounds
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
                    self.screen.fill(
                        CD[block],
                        pygame.Rect(
                            x * V['tile_size'],
                            y * V['tile_size'],
                            V['tile_size'], V['tile_size']
                        ))
            pygame.display.flip()

        def new_game(self) -> None:
            """
            Initializes the game
            """
            pygame.display.set_caption(
                f"Constalia: The Mark of a Hero [{VER['detailed']}]")
            self.screen = pygame.display.set_mode(self.size)
            # self.background = pygame.image.load()  # note to self place this
            # in draw_main()
            # Insert initializing objects here
except ModuleNotFoundError:
    pass
except NameError:
    pass


def legacy_graphics_engine(map: int, position: List[int]) -> None:
    """
    Prints a 7x7 grid map with the player as the center.
    The 7x7 grid is inflated to 21x21 for viewing convenience.
    For legacy purposes, if the new engine refuses to work.
    >>> legacy_graphics_engine(0, [6, 11])
    >>> legacy_graphics_engine(1, [5, 9])
    >>> legacy_graphics_engine(2, [10, 2])
    """
    m = mapz[map]
    View = []
    # Graphics generator
    for x in range(-3, 4):
        temp = []
        for y in range(-3, 4):
            try:
                temp.append(visual_dic[m.map_type][m.grid[position[0] + x]
                                                         [position[1] + y]])
            except IndexError:
                temp.append(visual_dic['outtaboundz'])
        View.append(temp)

    # Graphics printer
    print("\n╭─────────────────────╌╴╴"
          "\n│ Current location: {49}"
          "\n╰─────────────────────╌╴╴"
          "\n         <<[MAP]>>"
          "\n ┏━━━━━━━━━NORTH━━━━━━━━━┓ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}"
          "{4}{4}{4}{5}{5}{5}{6}{6}{6} ┃ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}"
          "{4}{4}{4}{5}{5}{5}{6}{6}{6} ┃ "
          "\n ┃ {7}{7}{7}{8}{8}{8}{9}{9}{9}{10}{10}{10}"
          "{11}{11}{11}{12}{12}{12}{13}{13}{13} ┃ "
          "\n ┃ {7}{7}{7}{8}{8}{8}{9}{9}{9}{10}{10}{10}"
          "{11}{11}{11}{12}{12}{12}{13}{13}{13} ┃ "
          "\n ┃ {14}{14}{14}{15}{15}{15}{16}{16}{16}"
          "{17}{17}{17}{18}{18}{18}{19}{19}{19}{20}{20}{20} ┃ "
          "\n W {14}{14}{14}{15}{15}{15}{16}{16}{16}"
          "{17}{17}{17}{18}{18}{18}{19}{19}{19}{20}{20}{20} E "
          "\n E {21}{21}{21}{22}{22}{22}{23}{23}{23}ɅꞈɅ{25}{25}{25}"
          "{26}{26}{26}{27}{27}{27} A "
          "\n S {21}{21}{21}{22}{22}{22}{23}{23}{23}YOU{25}{25}{25}"
          "{26}{26}{26}{27}{27}{27} S "
          "\n T {28}{28}{28}{29}{29}{29}{30}{30}{30}{31}{31}{31}"
          "{32}{32}{32}{33}{33}{33}{34}{34}{34} T "
          "\n ┃ {28}{28}{28}{29}{29}{29}{30}{30}{30}{31}{31}{31}"
          "{32}{32}{32}{33}{33}{33}{34}{34}{34} ┃ "
          "\n ┃ {35}{35}{35}{36}{36}{36}{37}{37}{37}{38}{38}{38}"
          "{39}{39}{39}{40}{40}{40}{41}{41}{41} ┃ "
          "\n ┃ {35}{35}{35}{36}{36}{36}{37}{37}{37}{38}{38}{38}"
          "{39}{39}{39}{40}{40}{40}{41}{41}{41} ┃ "
          "\n ┃ {42}{42}{42}{43}{43}{43}{44}{44}{44}{45}{45}{45}"
          "{46}{46}{46}{47}{47}{47}{48}{48}{48} ┃ "
          "\n ┃ {42}{42}{42}{43}{43}{43}{44}{44}{44}{45}{45}{45}"
          "{46}{46}{46}{47}{47}{47}{48}{48}{48} ┃ "
          "\n ┗━━━━━━━━━SOUTH━━━━━━━━━┛"
          "\n╭─────────────────────╌╴╴"
          "\n│ Stamina: {50}/{51}"
          "\n╰─────────────────────╌╴╴"
          .format(View[0][0], View[0][1], View[0][2], View[0][3],
                  View[0][4], View[0][5], View[0][6],  # Row 1
                  View[1][0], View[1][1], View[1][2], View[1][3],
                  View[1][4], View[1][5], View[1][6],  # Row 2
                  View[2][0], View[2][1], View[2][2], View[2][3],
                  View[2][4], View[2][5], View[2][6],  # Row 3
                  View[3][0], View[3][1], View[3][2], View[3][3],
                  View[3][4], View[3][5], View[3][6],  # Row 4
                  View[4][0], View[4][1], View[4][2], View[4][3],
                  View[4][4], View[4][5], View[4][6],  # Row 5
                  View[5][0], View[5][1], View[5][2], View[5][3],
                  View[5][4], View[5][5], View[5][6],  # Row 6
                  View[6][0], View[6][1], View[6][2], View[6][3],
                  View[6][4], View[6][5], View[6][6],  # Row 7
                  m.map_name, DV['stamina'],
                  p.max_stamina))


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
