"""
Constalia: The Mark of a Hero
Game by Jason [Urufu2000]
"""
from typing import Dict, List
import resources.graphics as graphics
import assets.texts as t
from resources.global_dic import controls as c
from resources.global_dic import variables as DV
from resources.global_dic import solids as solid_dic
from resources.global_dic import map_class as mapz
from resources import saveloadmaster as saving
import resources.player as p
from os import mkdir, path
import resources.eventulate as e
from chars import Firay
import msvcrt
''' For troubleshooting only
import sys
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

sys.excepthook = show_exception_and_exit
'''


def startup_folder_creations() -> None:
    """
    Creates necessary directories.
    """
    try:
        mkdir(path.expanduser('~\\Documents\\TMoaH'))
        if path.exists(path.expanduser('~\\Documents\\TMoaH')):
            mkdir(path.expanduser('~\\Documents\\TMoaH\\saves'))
            return
        mkdir(path.expanduser('~\\Downloads\\TMoaH'))
        if path.exists(path.expanduser('~\\Downloads\\TMoaH')):
            mkdir(path.expanduser('~\\Downloads\\TMoaH\\saves'))
            return
        mkdir(path.expanduser('~\\TMoaH'))
        mkdir(path.expanduser('~\\TMoaH\\saves'))
    except FileExistsError:
        return
    except Exception:
        input("Unknown error has occured! Please contact developer!")


def control_chooser() -> Dict[str, List[str]]:
    """
    Allows the player to choose control scheme
    """
    picked_control = c.control_null
    while picked_control == c.control_null:
        print(t.system_text.controls)
        input_control = input("Select controls: ")
        if input_control.isdigit():
            if int(input_control) in c.control_schemes:
                picked_control = c.control_schemes[int(input_control)]
            else:
                print(t.action_text.invalid_input)
        else:
            print(t.action_text.invalid_input)
    return picked_control


def successful_move() -> None:
    """
    Function that runs the needed stuff when successful action
    """
    print(t.action_text.valid_action)
    DV['stamina'] -= 1


def player_exhausted() -> None:
    """
    prints message when exhausted
    """
    print(Firay.expressions.e004)
    print(Firay.talking.t000)


def event_manager(y: int, x: int) -> bool:
    """
    Does action according to what the block_n is
    """
    lookup_mithavil = {
        2: e.false_check,  # house
        3: e.false_check,  # farm
        5: e.water_check,  # river/lake
        6: e.sign_check,  # signs
        7: e.door_check,  # locked door
        8: e.door_check,  # exit
        9: e.false_check  # boundary
    }
    lookup_interior = {
        1: e.char_check,  # character interaction
        2: e.bed_check,  # bed interaction
        3: e.table_check,  # table interaction
        4: e.door_check,  # Locked Vert door
        5: e.door_check,  # Locked Hori door
        8: e.door_check,  # exit
        9: e.false_check  # boundary
    }
    z = mapz[DV['m_id']].grid[y][x]
    w = mapz[DV['m_id']].map_type
    if z in solid_dic[w]:
        if w == 'Mithavil':
            lookup_mithavil[z](y, x)
        elif w == 'Mithavil Interior':
            lookup_interior[z](y, x)
        return True
    return False


# Game
if __name__ == '__main__':
    # startup_folder_creations()
    input(t.system_text.text)
    print("\n"*10)
    play_control = control_chooser()
    while True:
        graphics.main_graphics_engine(DV['m_id'], [DV['Y'], DV['X']])
        play_move = ''
        checked = False

        # checking input
        while not checked:
            print("Input: ")
            play_move = msvcrt.getch().decode("utf-8")
            for x in play_control:
                if play_move in play_control[x]:
                    checked = True
            if not checked:
                print(t.action_text.invalid_input)
                print("Controls:")
                for opti in play_control:
                    print("{0}: {1}".format(opti, play_control[opti]))

        # output of game based on input
        temp_id = DV['m_id']
        if play_move in play_control['Up']:
            if not event_manager(DV['Y'] - 1, DV['X']):
                DV['Y'] -= 1
                print(t.action_text.move_action)
        elif play_move in play_control['Down']:
            if not event_manager(DV['Y'] + 1, DV['X']):
                DV['Y'] += 1
                print(t.action_text.move_action)
        elif play_move in play_control['Left']:
            if not event_manager(DV['Y'], DV['X'] - 1):
                DV['X'] -= 1
                print(t.action_text.move_action)
        elif play_move in play_control['Right']:
            if not event_manager(DV['Y'], DV['X'] + 1):
                DV['X'] += 1
                print(t.action_text.move_action)
        elif play_move in play_control['Save']:
            saving.save_game()
        elif play_move in play_control['Load']:
            saving.load_game()
        elif play_move in play_control['Quit']:
            break
