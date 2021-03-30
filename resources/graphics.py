"""
Any "graphical" rendering and processing is done here!
Do NOT stuff text only stuff here, that's for the text module.
"""
from typing import List, Dict
from resources.global_dic import map_class as mapz
from resources.global_dic import visuals as visual_dic
from resources.global_dic import variables as DV
from resources import player as p
from assets import quests


Nyafim = False


def main_graphics_engine(map: int, position: List[int]) -> None:
    """
    Prints a 7x7 grid map with the player as the center.
    The 7x7 grid is inflated to 21x21 for viewing convenience.
    >>> main_graphics_engine(0, [6, 11])
    >>> main_graphics_engine(1, [5, 9])
    >>> main_graphics_engine(2, [10, 2])
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
                  p.Stamina.max_stamina))


def battle_graphics_engine(map: int, position: List[int]) -> None:
    """
    A separate graphics engine made for battle. Just a little entry point
    once I get to the point of coding the battle sequence in.
    This is mostly just for reminding me though.
    """
    pass


def quest_output() -> None:
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
