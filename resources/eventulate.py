"""
Event handler. Handle with care. Legacy only.
"""
import msvcrt
from resources.global_dic import variables as DV
from resources.global_dic import doors
from resources.global_dic import interactables as i
from resources.global_dic import LOOP_FILES as LF
from resources.engine import Engineer
from resources import jukebox as JB
from assets.quests import run_quest
from resources.char import Player
import assets.texts as t
from chars.Firay import *
import chars.John as John
import chars.Ravia as Ravia


def bed(action_id: str) -> None:
    """
    For bed interactions
    """
    if action_id == 'firay_bed_interact':
        print(expressions.e000)
        input(interacting.i001)
        print(t.action_text.ask_sleeping)
        userin = msvcrt.getch().decode("utf-8")
        while userin.lower() not in ['y', 'n']:
            print(t.action_text.invalid_input)
            print(t.action_text.ask_sleeping)
            userin = msvcrt.getch().decode("utf-8")
        if userin.lower() == 'y':
            # DV['stamina'] = Player.stamina_recovery(DV['stamina'], 'bed')
            print('\n\n')
            print(t.action_text.done_sleeping)
        elif userin.lower() == 'n':
            print('\n\n')

    elif action_id == 'rubi_bed_interact':
        print(expressions.e000)
        input(interacting.i002)
        print(expressions.e002)
        input(interacting.i003)
    else:  # Typical bed interaction
        print(expressions.e000)
        input(interacting.i011)


def false(action_id: str) -> None:
    """
    Just prints, is all. For checks that don't need anything to be done.
    """
    print(t.action_text.run_into_solid)


def table(action_id: str) -> None:
    """
    For interaction with tables
    """
    if action_id == 'home_table':
        print(expressions.e000)
        input(interacting.i004)
        print(expressions.e002)
        input(interacting.i005)
        print(expressions.e003)
        input(interacting.i006)
    else:  # Typical table interaction
        print(expressions.e000)
        input(interacting.i010)


def door(action_id: str) -> None:
    """
    For interaction with doors

    WARNING: Hardcoded
    """
    if action_id == 'none':
        pass
    elif action_id == 'mithavil - home':
        if DV['m_id'] == 0:
            DV['m_id'], DV['Y'], DV['X'] = 1, 10, 9
            JB.jam(LF['home'])
        else:
            DV['m_id'], DV['Y'], DV['X'] = 0, 9, 46
            JB.jam(LF['mithavil'])
    elif action_id == 'mithavil - ravia':
        if DV['m_id'] == 0:
            DV['m_id'], DV['Y'], DV['X'] = 2, 4, 1
            JB.jam(LF['ravia'])
        else:
            DV['m_id'], DV['Y'], DV['X'] = 0, 20, 51
            JB.jam(LF['mithavil'])
    else:
        pass


def char(action_id: str) -> None:
    """
    For interaction with characters
    """
    if action_id == 'talk_john':
        print(expressions.e000)
        input(talking.t010)
        print(John.expressions.e000)
        input(John.talking.t000)
        print(expressions.e005)
        input(talking.t011)
        print(John.expressions.e001)
        input(John.talking.t001)
    elif action_id == 'talk_rubi':
        print(expressions.e000)
        input(talking.t009)
    elif action_id == 'talk_ravia':
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
    else:
        pass


def sign(action_id: str) -> None:
    if action_id == 'mith_locan_news':
        print(t.placeholder.placeholder_sign)
    elif action_id == 'mith_direction':
        print(t.placeholder.placeholder_sign)
    else:  # Typical sign interaction
        print(t.placeholder.placeholder_sign)


def water(action_id: str) -> None:
    # Generic water interaction for now. No, there's no witches.
    print(expressions.e000)
    input(interacting.i007)
    print(expressions.e002)
    input(interacting.i008)
    print(expressions.e002)
    input(interacting.i009)

class temp_i(Engineer):
    """
    Temporary class that contains text interactions.
    Used for slowly converting the command line output stuff to pygame stuff
    """
    def door(self, id: str) -> None:
        pass  # reserved for jukebox
    # TODO  change how text is handled fundamentally
    def bed(self, id: str) -> None:
        if id == 'firay_bed_interact':
            print("firay bed triggered")
            self.add_text(
                expressions.e000, interacting.i001)
            '''
            speech.append(expressions.e000)
            speech.append(interacting.i001)
            '''
        elif id == 'rubi_bed_interact':
            print("rubi bed triggered")
            self.add_text(
                expressions.e000, interacting.i002,
                expressions.e002, interacting.i003)
        else:  # Typical bed interaction
            self.add_text(
                expressions.e000, interacting.i011)
        DV['is_talking'] = True
        self.cue_text()

    def table(self, id: str) -> None:
        if id == 'home_table':
            self.add_text(
                expressions.e000, interacting.i004,
                expressions.e002, interacting.i005, 
                expressions.e003, interacting.i006)
        else:  # Typical table interaction
            self.add_text(
                expressions.e000, interacting.i010)
        DV['is_talking'] = True
        self.cue_text()

    def character(self, id: str) -> None:  # all typical interactions
        if id == 'talk_john':
            print("john triggered")
            self.add_text(
                expressions.e000, talking.t010,
                John.expressions.e000, John.talking.t000,
                expressions.e005, talking.t011,
                John.expressions.e001, John.talking.t001)
        elif id == 'talk_rubi':
            print("rubi triggered")
            self.add_text(
                expressions.e000, talking.t009)
        elif id == 'talk_ravia':
            print("ravia triggered")
            self.add_text(
                Ravia.expressions.e000, Ravia.talking.t000,
                expressions.e000, talking.t014,
                Ravia.expressions.e001, Ravia.talking.t006,
                expressions.e000, talking.t015,
                Ravia.expressions.e000, Ravia.talking.t007,
                expressions.e000, talking.t015,
                Ravia.expressions.e002, Ravia.talking.t007,
                expressions.e000, talking.t016,
                Ravia.expressions.e001, Ravia.talking.t008)
        else:
            return
        DV['is_talking'] = True
        self.cue_text()

    def false(self, id: str) -> None:
        print(t.action_text.run_into_solid)

class apply_interactions:  # for applying interactions(usually outputs text)
    def door(id: str) -> None:
        pass  # reserved for jukebox

    def bed(id: str) -> None:
        if id == 'firay_bed':
            print(expressions.e000)
            input(interacting.i001)
        elif id == 'rubi_bed':
            print(expressions.e000)
            input(interacting.i002)
            print(expressions.e002)
            input(interacting.i003)
        else:  # Typical bed interaction
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
        else:  # Typical table interaction
            print(expressions.e000)
            input(interacting.i010)

    def character(id: str) -> None:  # all typical interactions
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
        else:  # Typical sign interaction
            print(t.placeholder.placeholder_sign)

    def water(id: str) -> None:
        # Generic water interaction for now. No, there's no witches.
        print(expressions.e000)
        input(interacting.i007)
        print(expressions.e002)
        input(interacting.i008)
        print(expressions.e002)
        input(interacting.i009)
