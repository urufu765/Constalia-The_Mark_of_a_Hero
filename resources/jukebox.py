"""
Music playing shenanigans
"""
from pygame import mixer
from resources.global_dic import LOOP_FILES as LF


def jam(file_location=LF[0]) -> None:
    """
    Plays music on loop
    """
    mixer.init()
    mixer.music.stop()
    # TODO: Don't play anything if it doesn't exist or sth
    mixer.music.load(file_location)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
