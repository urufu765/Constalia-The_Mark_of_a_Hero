"""
Constalia: The Mark of a Hero
Game by [URUFU765]
"""
from resources import engine  # Graphics
import assets.texts as t  # Text
from resources.global_dic import controls as c  # Controls
from resources.global_dic import variables as DV  # Global variables
from resources.global_dic import pygame_variables as PV  # Pygame variables
from resources.global_dic import map_to_values as mtv
from resources import saveloadmaster as saving  # Saving files
from resources.char import Player as p  # Player
from os import mkdir, path  # Saving
from resources.eventulate import temp_i as e  # Event manager
from chars import Firay  # Firay text
import pygame as pG

# Game is running?
GAME = True

# Debug Mode (new_yeetable_additions_for_insurance_measures)
Nyafim = False

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


def event_manager(engi: engine.Engineer, y: int, x: int):
    """
    Does action according to what the block_n is and using a dictionary

    TODO: Change code so it's not hard coded
    """
    lookup_event = {
        't_wall': e.false,
        't_water': e.false,
        't_sand': e.false,
        'o_table': e.table,
        'o_bed': e.bed,
        'o_door': e.door,
        'c_generic': e.character,
        'w': e.false
    }
    try:
        value = mtv[engi.get_value(y, x)]
        lookup_event[value[0]](engi, value[2])
        print(value[3])
        return value[3]
    except KeyError:
        print("keyerror")
        return False


def event_handler(engi: engine.Engineer) -> bool:
    """
    Applies the correct output using events and keypresses
    Default is WASD and arrows and will always be WASD and arrows
    """
    for event in pG.event.get():
        if event.type == pG.QUIT:
            return False
        elif event.type == pG.KEYDOWN:
            if DV['is_talking']:
                if event.key == pG.K_RETURN:
                    if engi.get_i() + 1 >= engi.get_l() - 1:
                        engi.reset_text()
                        DV['is_talking'] = False
                    else:
                        engi.cue_text()
                        engi.cue_text()
            elif event.key == pG.K_q:
                pass  # quest output
            elif event.key == pG.K_z:
                pass  # save
            elif event.key == pG.K_x:
                pass  # load
            else:
                if event.key == pG.K_w or event.key == pG.K_UP:
                    if not event_manager(engi, DV['Y'] - 1, DV['X']):
                        DV['Y'] -= 1
                elif event.key == pG.K_s or event.key == pG.K_DOWN:
                    if not event_manager(engi, DV['Y'] + 1, DV['X']):
                        DV['Y'] += 1
                elif event.key == pG.K_a or event.key == pG.K_LEFT:
                    if not event_manager(engi, DV['Y'], DV['X'] - 1):
                        DV['X'] -= 1
                elif event.key == pG.K_d or event.key == pG.K_RIGHT:
                    if not event_manager(engi, DV['Y'], DV['X'] + 1):
                        DV['X'] += 1
    return True


# Game
if __name__ == '__main__':
    startup_folder_creations()
    play_control = c.control_schemes[3]  # WASD default
    pG.init()
    main_game = engine.Engineer(True)
    main_game.new_game()
    while GAME:
        main_game.draw_main()  # unbound but that's okay
        pG.time.wait(1000//PV['FPS'])
        GAME = event_handler(main_game)
