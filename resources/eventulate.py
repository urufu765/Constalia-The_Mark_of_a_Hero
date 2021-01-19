import msvcrt
from resources.global_dic import variables as DV
from resources.global_dic import doors
from resources.global_dic import interactables as i
from resources.player import *
import assets.texts as t
from chars.Firay import *
import chars.John as John
import chars.Ravia as Ravia


def false_check(y: int, x: int) -> None:
    """
    Just prints, is all.
    """
    print(t.action_text.run_into_solid)


def door_check(y: int, x: int) -> None:
    """
    Checks if player is standing on a door and applies action
    """
    try:
        dest = doors['{}-{}-{}'.format(DV['m_id'], y, x)]
        if not dest[1]:
            DV['m_id'], DV['Y'], DV['X'] = dest[2], dest[3], dest[4]
        else:
            apply_interactions.door(dest[0])
            print(t.action_text.door_locked)
    except KeyError:
        print(t.action_text.door_locked)


def bed_check(y: int, x: int) -> None:
    """
    Finds the door in question and applies appropriate action
    """
    try:
        bed = i['{}-{}-{}'.format(DV['m_id'], y, x)]
        if bed[2]:
            apply_interactions.bed(bed[0])
            print(t.action_text.ask_sleeping)
            userin = msvcrt.getch().decode("utf-8")
            while userin.lower() not in ['y', 'n']:
                print(t.action_text.invalid_input)
                print(t.action_text.ask_sleeping)
                userin = msvcrt.getch().decode("utf-8")
            if userin.lower() == 'y':
                DV['stamina'] = Stamina.stamina_recovery(
                    Stamina, DV['stamina'], 'bed')
                print('\n\n')
                print(t.action_text.done_sleeping)
            elif userin.lower() == 'n':
                print('\n\n')
        else:
            apply_interactions.bed(bed[0])
    except KeyError:
        print(t.action_text.run_into_solid)


def table_check(y: int, x: int) -> None:
    """
    Checks tables and applies action
    """
    try:
        tables = i['{}-{}-{}'.format(DV['m_id'], y, x)]
        if tables[2]:  # for when there's something on the table
            pass
        else:
            apply_interactions.table(tables[0])
    except KeyError:
        print(t.action_text.run_into_solid)


def char_check(y: int, x: int) -> None:
    """
    Checks NPC and applies action
    """
    try:
        characs = i['{}-{}-{}'.format(DV['m_id'], y, x)]
        if characs[2]:  # for something, haven't decided
            pass
        else:
            apply_interactions.character(characs[0])
    except KeyError:
        print(t.action_text.run_into_solid)


def sign_check(y: int, x: int) -> None:
    """
    Checks signs
    """
    try:
        signs = i['{}-{}-{}'.format(DV['m_id'], y, x)]
        if signs[2]:  # for if there's something to do with signs
            pass
        else:
            apply_interactions.sign(signs[0])
    except KeyError:
        print(t.action_text.run_into_solid)


def water_check(y: int, x: int) -> None:
    """
    Checks water interaction. Coordinates don't matter for now
    """
    apply_interactions.water('')


class apply_interactions:
    def door(id: str) -> None:
        pass

    def bed(id: str) -> None:
        if id == 'firay_bed':
            print(expressions.e000)
            input(interacting.i001)
        elif id == 'rubi_bed':
            print(expressions.e000)
            input(interacting.i002)
            print(expressions.e002)
            input(interacting.i003)
        else:
            print(expressions.e000)
            input(interacting.i011)

    def table(id: str) -> None:
        if id == 'home_table':
            print(expressions.e000)
            input(interacting.i004)
            print(expressions.e002)
            input(interacting.i005)
            print(expressions.e003)
            input(interacting.i006)
        else:
            print(expressions.e000)
            input(interacting.i010)

    def character(id: str) -> None:
        if id == 'john':
            print(expressions.e000)
            input(talking.t010)
            print(John.expressions.e000)
            input(John.talking.t000)
            print(expressions.e005)
            input(talking.t011)
            print(John.expressions.e001)
            input(John.talking.t001)
        elif id == 'rubi':
            print(expressions.e000)
            input(talking.t009)
        elif id == 'ravia':
            print(Ravia.expressions.e000)
            input(Ravia.talking.t000)
            print(expressions.e000)
            input(talking.t014)
            print(Ravia.expressions.e001)
            input(Ravia.talking.t006)
            print(expressions.e000)
            input(talking.t015)
            print(Ravia.expressions.e000)
            input(Ravia.talking.t007)
            print(expressions.e000)
            input(talking.t015)
            print(Ravia.expressions.e002)
            input(Ravia.talking.t007)
            print(expressions.e000)
            input(talking.t016)
            print(Ravia.expressions.e001)
            input(Ravia.talking.t008)

    def sign(id: str) -> None:
        if id == 'mith_locan_news':
            print(t.placeholder.placeholder_sign)
        elif id == 'mith_direction':
            print(t.placeholder.placeholder_sign)
        else:
            print(t.placeholder.placeholder_sign)

    def water(id: str) -> None:
        print(expressions.e000)
        input(interacting.i007)
        print(expressions.e002)
        input(interacting.i008)
        print(expressions.e002)
        input(interacting.i009)