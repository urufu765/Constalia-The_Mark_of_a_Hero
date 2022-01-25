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
from resources.global_dic import SPEECH_BOX as SB
from resources.char import Player as p
from resources import jukebox as JB
from resources import char
from assets import quests
import pygame
import pygame.freetype
from resources import mapper

# Debugger
Nyafim = False


class Engineer:
    # window
    size: Tuple[int, int]
    width: int
    height: int
    screen: Optional[pygame.Surface]
    text_mac: pygame.freetype.Font  # 'short' for Text machine
    w_tiles: int
    l_tiles: int
    tiles_number: Tuple[int, int]
    background: Optional[pygame.Surface]

    __characters: List[char.Characters]
    __run_stat: bool
    __map_view: List[List[any]]  # Will convert to List[str] later
    __text_view: List[any]  # See the function it's used in to know how to use
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
        self.text_mac = pygame.freetype.Font(
            'assets/font/CONSOLA.TTF', (V['tile_size']*2.1)/5)
        self.text_mac.pad = True
        self.text_mac.antialiased = False
        self.text_mac.origin = False

        # Storing speaking texts. First value is ALWAYS the index
        # Also __text_view always follows Face(index n), Text(index n*2)
        self.__text_view = [0]  # Important: RESET INDEX AND EMPTY AFTER EVERY CONVERSATION

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
        if DV['is_talking']:
            self.draw_text()
        pygame.display.flip()

    def reset_text(self) -> None:
        """
        Resets the text storage for next interaction
        """
        self.__text_view = [0]

    def adt_text(
            self, protagonist: bool, speech: List[str], lines=0, cont=False):
        """
        Simpler version of set text. Both versions are unused atm
        """
        line_num = lines
        if line_num == 0:
            if len(speech) <= 5:
                line_num = len(speech)
            else:
                line_num = len(speech) // 5
        for i, line in enumerate(speech):
            if (i % line_num) == 0:
                self.__text_view.append([
                    'main_sta' if protagonist else 'side_sta', ])
            self.__text_view.append([
                'main_mid' if protagonist else 'side_mid',
                SB['main_mid' if protagonist else 'side_mid'] 
                % (line + (' ' * (36 - len(line))))
            ])
            if (i % line_num) == 0:
                if (len(speech) - i) > line_num or cont:
                    self.__text_view.append([
                        'main_con' if protagonist else 'side_con', None])
                else:
                    self.__text_view.append([
                        'main_end' if protagonist else 'side_end', None])


    def set_text(self, protagonist: bool, speech: str, lines=0, cont=False) -> int:
        """
        Adds the text to the text storage. Takes whether it's the
        protagonist speaking or not and their speech as the argument.
        Third parameter is for forcing a certain number of lines. Otherwise
        it's automatically calculated.
        Fourth parameter is for clarifying whether to just have continuing
        speech boxes.
        Outputs box height.
        """
        '''How it works (internally):
        The way the speech is placed in follows some rules:
        1. Each line must be at most 36 characters long.
        2. Each box is at most 5 lines big, and the size does
            not switch until it's the next character talking
        3. The talk box is formatted as follows:
            0: index {used for checking which interaction to show}
            1: [top text border id, number of lines]
            2: [mid text border id, line {preformated}]
            ...
            3~: [end text border, null] {haven't found use yet for null}
            ~?: character art {kept as legacy, will change later}
        '''
        line_num = lines

        # Takes care of converting one big string into a wall of text
        word_list = speech.split(" ")
        word_line = []
        while len(word_list) > 0:
            box = True
            temp = ''
            while box and len(word_list) > 0:
                if len(temp + ' ' + word_list[0]) < 36:
                    temp += ' ' + word_list.pop(0)
                else:
                    box = False
            word_line.append(temp)

        # calculates the number of lines it should use
        if line_num == 0:
            if len(word_line) <= 5:
                line_num = len(word_line)
            else:
                line_num = len(word_line) // 5
        for i, line in enumerate(word_line):
            if (i % line_num) == 0:
                self.__text_view.append([
                    'main_sta' if protagonist else 'side_sta', line_num])
            self.__text_view.append([
                'main_mid' if protagonist else 'side_mid',
                SB['main_mid' if protagonist else 'side_mid'] 
                % (line + (' ' * (36 - len(line))))
            ])
            if (i % line_num) == 0:
                if (len(word_line) - i) > line_num or cont:
                    self.__text_view.append([
                        'main_con' if protagonist else 'side_con', None])
                else:
                    self.__text_view.append([
                        'main_end' if protagonist else 'side_end', None])
        return line_num

    def add_text(self, *args):
        """
        A legacy way of adding text, nothing fancy here
        """
        for text in args:
            self.__text_view.append(text)
    
    def cue_text(self):
        """
        Cue up text to be displayed.
        """
        self.__text_view[0] += 1

    def get_i(self):
        """
        Gets the index of the current text
        """
        return self.__text_view[0]

    def get_l(self):
        """
        Gets the length of the text
        """
        return len(self.__text_view)

    def draw_text(self) -> None:
        """
        Draws the text on the screen
        Perhaps use freetype instead of font
        """
        temp_lines = self.__text_view[self.__text_view[0]].split('\n')
        if Nyafim: self.debug_text()
        for index, line in enumerate(
                self.__text_view[self.__text_view[0] + 1].split('\n')):
            if Nyafim:
                print("index:", index, "line:", temp_lines[index+1])
                print("index:", index, "line:", line)
            self.screen.blit(self.text_mac.render(
                    temp_lines[index+1],(255,255,255),(0,0,0))[0],
                (((self.w_tiles/2) - 5) * V['tile_size'],
                (self.l_tiles - (5 - (0.5 * index))) * V['tile_size']))
            self.screen.blit(self.text_mac.render(
                    line,(255,255,255),(0,0,0))[0],
                (((self.w_tiles/2) - 5) * V['tile_size'],
                (self.l_tiles - (2.5 - (0.5 * index))) * V['tile_size']))



        '''
        # Top half box
        self.screen.fill(
            CD['o'],
            pygame.Rect(
                ((self.w_tiles/2)-5) * V['tile_size'],
                (self.l_tiles-5) * V['tile_size'],
                1.75 * V['tile_size'], 1.5 * V['tile_size']
            )
        )
        # Bottom half box
        self.screen.fill(
            CD['o'],
            pygame.Rect(
                ((self.w_tiles/2)-5) * V['tile_size'],
                (self.l_tiles-3.5) * V['tile_size'],
                10 * V['tile_size'], 3.5 * V['tile_size']
            )
        )
        # Text TODO optimize if possible by only rendering the text once
        temp_lines = self.__text_view[self.__text_view[0]].split('\n')
        for index, line in enumerate(
                self.__text_view[self.__text_view[0] * 2].split('\n')):
            self.screen.blit(self.text_mac.render(
                    temp_lines[index+1],(255,255,255))[0],
                (((self.w_tiles/2) - 5) * V['tile_size'],
                (self.l_tiles - (5 - (0.5 * index))) * V['tile_size']))
            self.screen.blit(self.text_mac.render(
                    line,(255,255,255))[0],
                (((self.w_tiles/2) - 5) * V['tile_size'],
                (self.l_tiles - (2.5 - (0.5 * index))) * V['tile_size']))
        
        self.__text_view.render_to(self.screen,
            (((self.w_tiles/2)-5) * V['tile_size'],
            (self.l_tiles-5) * V['tile_size']),
            (S[S[0]] + "\n" + S[S[0] * 2]), (255,255,255))
        # self.screen.blit(self.__text_view.render(
        #     (S[S[0]] + "\n" + S[S[0] * 2]), (255,255,255)),
        #     (((self.w_tiles/2)-5) * V['tile_size'],
        #     (self.l_tiles-5) * V['tile_size']))
        '''

    def debug_text(self):
        """
        For debugging text (with out of range stuff) purposes
        """
        for x in self.__text_view:
            print("-", x)
        for y in self.text_mac.get_sizes():
            print("+", y)
        print(self.text_mac.get_sized_height())

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
