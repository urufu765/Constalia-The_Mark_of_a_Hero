"""
Constalia: The Mark of a Hero
Game by [URUFU765]
"""
from typing import Dict, List
from resources import engine  # Graphics
import assets.texts as t  # Text
from resources.global_dic import controls as c  # Controls
from resources.global_dic import variables as DV  # Global variables
from resources.global_dic import solids as solid_dic  # Solid codes
from resources.global_dic import map_class as mapz  # Map data
from resources import saveloadmaster as saving  # Saving files
import resources.player as p  # Player
from os import mkdir, path  # Saving
import resources.eventulate as e  # Event manager
from chars import Firay  # Firay text

# Game is running?
GAME = True

# Debug Mode (new_yeetable_additions_for_insurance_measures)
Nyafim = False

# Toggle this to False once Pygame engine is ready for launch
LEGACY = True
try:
    import pygame
except ModuleNotFoundError:
    LEGACY = True

if Nyafim:
    # For troubleshooting only
    import sys

    def show_exception_and_exit(exc_type, exc_value, tb):
        import traceback
        traceback.print_exception(exc_type, exc_value, tb)
        input("Press key to exit.")
        sys.exit(-1)

    sys.excepthook = show_exception_and_exit


def startup_folder_creations() -> None:
    """
    Creates necessary directories.
    """
    try:
        mkdir(path.expanduser('~\\Documents\\TMoaH'))
        if path.exists(path.expanduser('~\\Documents\\TMoaH')):
            mkdir(path.expanduser('~\\Documents\\TMoaH\\saves'))
            return  # return if folder has been created successfully in docs
        mkdir(path.expanduser('~\\Downloads\\TMoaH'))
        if path.exists(path.expanduser('~\\Downloads\\TMoaH')):
            mkdir(path.expanduser('~\\Downloads\\TMoaH\\saves'))
            return  # return if folder has been created successfully in dls
        mkdir(path.expanduser('~\\TMoaH'))
        mkdir(path.expanduser('~\\TMoaH\\saves'))
    except FileExistsError:
        return  # if the directory already exists
    except Exception:
        input("Unknown error has occured! Please contact developer!")


def legacy_control_chooser() -> Dict[str, List[str]]:
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
    Function that runs the needed stuff when successful action.
    This function may move to a different file.
    """
    print(t.action_text.valid_action)
    DV['stamina'] -= 1


def player_exhausted() -> None:
    """
    prints message when exhausted
    This function may move to a different file.
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


def legacy_input_handler(play_control: Dict[str, List[str]]) -> str:
    """
    Handles user input and outputs it
    """
    import msvcrt
    checked = False
    p_input = ''
    while not checked:
        print("Input: ")
        p_input = msvcrt.getch().decode("utf-8")
        for x in play_control:
            if p_input in play_control[x]:
                checked = True
        if not checked:
            print(t.action_text.invalid_input)
            print("Controls:")
            for opti in play_control:
                print("{0}: {1}".format(opti, play_control[opti]))
    return p_input


def legacy_event_handler(play_move: str) -> bool:
    """
    Applies the correct output using the string input
    Output is only used to determine whether to stop the game or not.
    """
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
    # Direction output end
    elif play_move in play_control['Quest']:
        # Note to self: Add a way to switch quests.
        engine.legacy_quest_output()
    elif play_move in play_control['Save']:
        saving.save_game()
    elif play_move in play_control['Load']:
        saving.load_game()
    elif play_move in play_control['Quit']:
        return False
    return True


# Game
if __name__ == '__main__':
    startup_folder_creations()
    play_control = c.control_schemes[3]  # WASD default
    if LEGACY:
        input(t.system_text.text)
        print("\n"*10)
        play_control = legacy_control_chooser()  # prompts player to choose
    while GAME:
        if not LEGACY:
            engine.engineer()
        else:
            engine.legacy_graphics_engine(DV['m_id'], [DV['Y'], DV['X']])
            GAME = legacy_event_handler(legacy_input_handler(play_control))
