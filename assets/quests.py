"""
Contains quests
"""
from resources.global_dic import quests as DQ
from resources.global_dic import interactables as DI
from resources.player import Inventory as i
from resources.player import Stamina as s
from typing import Dict
import chars.Rubi as Rubi
import chars.Ravia as Ravia
import chars.Firay as Firay
import assets.texts as t
'''
Inactive: Quest not activated
Active: Quest currently active
Complete: Quest completed
Incomplete: Quest stopped and resumable
Locked: Quest not doable(yet/anymore)
'''


Nyafim = False


class quests:
    """
    A quest object meant to store each quest as an object when accessed.
    """
    quest_id = str
    quest_type = str
    quest_status = str
    step = int

    def __init__(self, quest_id: str, quest_type: str):
        self.quest_id = quest_id
        self.quest_type = quest_type
        self.quest_status = DQ[quest_id][1]
        self.step = DQ[quest_id][0]

    def sanity_check(self) -> bool:
        """
        Checks whether the quest can be started
        """
        if self.quest_status in ['Inactive', 'Incomplete']:
            # For Incomplete, implement a way for the player to pause the
            # quest and resume later
            return True
        return False

    def active_quest(self, quest_steps: Dict[str, object],
                     inter_id: str) -> None:
        """
        May not be used.
        """
        if Nyafim:
            print("<quests: active_quest triggered>")
        self.q_update()
        quest_steps[self.step](inter_id)

    def progress_quest(self, quest_steps: Dict[str, object], inter_id) -> None:
        """
        Progresses the quest
        """
        if Nyafim:
            print("<quests: progress_quest triggered>")
        try:
            self.step += 1
            self.q_update()
            quest_steps[self.step](inter_id)
        except KeyError:
            if Nyafim:
                print("<quests: progress_quest KeyError triggered>")
            self.quest_status = 'Complete'
            self.q_update()

    def quest_placeholder(self, inter_id: str) -> None:
        """
        Does nothing but act as a placeholder
        """
        raise NotImplementedError

    def q_update(self) -> None:
        """
        Does nothing, only a reference that's usually overriden
        """
        raise NotImplementedError


class get_clear_leaf(quests):
    """
    A quest for getting a leaf from Ravia, given by Rubi
    """
    quest_steps: Dict[str, object]
    step: int
    name: str
    quest_id = str
    quest_type = str
    quest_status = str
    description: str
    talked_rubi: str
    talked_ravia: str

    def __init__(self):
        quests.__init__(self, 'get_leaf', 'main')
        self.quest_steps = {
            0: self.get_quest_rubi,
            1: self.get_leaf_ravia,  # Interacting with Ravia
            2: self.give_leaf_rubi  # Bringing the leaf back to Rubi
        }
        self.name = 'Get Clear Leaf'
        self.description = ('Rubi asks you to get a Clear Leaf from Ravia to'
                            + ' complete her latest potion brew')
        self.talked_ravia = DQ[self.quest_id][2][0]
        self.talked_rubi = DQ[self.quest_id][2][1]

    def cont_quest(self, inter_id: str) -> None:
        """
        Used mostly for updating quest during steps
        """
        if Nyafim:
            print("<get_clear_leaf: cont_quest triggered>")
        self.quest_steps[self.step](inter_id)

    def q_update(self):
        """
        Updates quest status in quest dictionary
        """
        if Nyafim:
            print("<get_clear_leaf: q_update triggered>")
        DQ[self.quest_id][0] = self.step
        DQ[self.quest_id][1] = self.quest_status
        DQ[self.quest_id][2][0] = self.talked_ravia
        DQ[self.quest_id][2][1] = self.talked_rubi

    def get_quest_rubi(self, inter_id: str) -> None:
        """
        Getting the quest from Rubi
        """
        if self.sanity_check:
            if Nyafim:
                print("<get_clear_leaf: Sanity check cleared>")
            # Asking Firay to do a damn fetch quest
            # Main Dialogue Start
            print(Rubi.expressions.e000)
            input(Rubi.talking.t000)
            print(Firay.expressions.e000)
            input(Firay.talking.t001)
            print(Rubi.expressions.e001)
            input(Rubi.talking.t001)
            print(Rubi.expressions.e000)
            input(Rubi.talking.t002)
            print(Firay.expressions.e000)
            input(Firay.talking.t002)
            print(Rubi.expressions.e000)
            input(Rubi.talking.t003)
            # Main Dialogue End
            player_in = input(t.quest_text.quest_accept)
            if player_in.lower() == 'y':
                # Accepting the damn fetch quest
                if Nyafim:
                    print("<get_clear_leaf: Firay Accepts Quest>")
                print(Firay.expressions.e000)
                input(Firay.talking.t003)  # may split the text up
                # print(t.quest_text.quest_Start) (not implemented yet)
                self.quest_status = 'Active'
                self.talked_rubi = 'on the way'
                self.progress_quest(self.quest_steps, inter_id)
            else:
                # Declining the damn fetch quest
                # Add dialogue for this
                if Nyafim:
                    print("<get_clear_leaf: Firay Declines Quest>")
        else:  # This should never happen.
            print("Error! Error?! Error at get_quest_rubi! AaaA!")
        self.q_update()

    def get_leaf_ravia(self, inter_id: str) -> None:
        """
        Getting the leaf from Ravia
        """
        if Nyafim:
            print("<get_clear_leaf: Quest successfully bridged to stage 1>")
        if self.quest_status == 'Active':
            if inter_id == 'rubi' and self.talked_rubi == 'on the way':
                # Debrief on the location of said item
                # Main Dialogue Start
                print(Rubi.expressions.e002)
                input(Rubi.talking.t004)
                print(Rubi.expressions.e003)
                input(Rubi.talking.t005)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t006)
                # Main Dialogue End
                self.talked_rubi = 'not now'
                DI['2-6-7'][2] = True  # Unlock Ravia interactions
            elif inter_id == 'rubi' and self.talked_rubi == 'not now':
                # tell Firay where he can find the leaf again
                # Note to self: redo dialogue
                if Nyafim:
                    print("<get_clear_leaf: Talked to rubi again at stage 1>")
                print(Rubi.expressions.e001)
                input(Rubi.talking.t007)
            elif inter_id == 'ravia' and self.talked_ravia == 'n':
                # Give Firay the leaf
                # Implement items for the true experience lol
                # Here's where you get the item.
                if Nyafim:
                    print("<get_clear_leaf: Talked to ravia at stage 1>")
                print(Ravia.expressions.e001)
                input(Ravia.talking.t000)
                print(Firay.expressions.e000)
                input(Firay.talking.t012)
                print(Ravia.expressions.e000)
                input(Ravia.talking.t001)
                print(Ravia.expressions.e000)
                input(Ravia.talking.t002)
                print(Firay.expressions.e000)
                input(Firay.talking.t013)
                print(Ravia.expressions.e001)
                input(Ravia.talking.t003)
                self.talked_ravia = 'talked to'
                self.progress_quest(self.quest_steps, inter_id)
            else:  # This should never happen
                print("Error! Error at get_leaf_ravia!")
        self.q_update()

    def give_leaf_rubi(self, inter_id: str) -> None:
        """
        Giving the leaf to Rubi
        """
        if Nyafim:
            print("<get_clear_leaf: Successfully bridged to stage 2>")
        if self.quest_status == 'Active':
            if inter_id == 'ravia' and self.talked_ravia == 'talked to':
                # tell Firay to f*** off
                if Nyafim:
                    print("<get_clear_leaf: talked to ravia again at stage 2>")
                print(Ravia.expressions.e001)
                input(Ravia.talking.t004)
            elif inter_id == 'rubi' and self.talked_rubi == 'not now':
                # Change condition to searching for item in inventory later
                # get the leaf from Firay and end quest
                if Nyafim:
                    print("<get_clear_leaf: talked to rubi to finish quest>")
                # Main Dialogue Start
                print(Firay.expressions.e000)
                input(Firay.talking.t004)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t008)
                print(Firay.expressions.e005)
                input(Firay.talking.t005)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t009)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t010)
                print(Firay.expressions.e000)
                input(Firay.talking.t006)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t011)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t012)
                print(Rubi.expressions.e004)
                input(Rubi.talking.t013)
                print(Firay.expressions.e005)
                input(Firay.talking.t007)
                print(Rubi.expressions.e000)
                input(Rubi.talking.t014)
                print(Firay.expressions.e000)
                input(Firay.talking.t008)
                # Main Dialogue End
                # Here's where the item is taken from your inventory
                DI['1-9-7'][2] = False
                '''It isn't recommended to disable a character's
                interactability, but it's okay here since Rubi will
                probably never be used again.'''
                self.progress_quest(self.quest_steps, inter_id)
        self.q_update()


def run_quest(char_id: str) -> bool:
    """
    Starts or resume quests
    """
    # For functional dictionary use
    q_lookup_table = {
        'get_leaf': get_clear_leaf
    }
    for quests in DQ:
        if DQ[quests][1] == 'Inactive':
            if Nyafim:
                print("<: run_quest Inactive triggered>")
            current_quest = q_lookup_table[quests]()
            current_quest.cont_quest(char_id)
            return True
        if DQ[quests][1] == 'Active':  # Both do the same thing for now idk
            if Nyafim:
                print("<: run_quest Active triggered>")
            current_quest = q_lookup_table[quests]()
            current_quest.cont_quest(char_id)
            return True
    return False
