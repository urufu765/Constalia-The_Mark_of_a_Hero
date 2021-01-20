"""
Contains quests
"""
'''
Inactive: Quest not activated
Active: Quest currently active
Complete: Quest completed
Incomplete: Quest stopped and resumable
Locked: Quest not doable
'''


class get_clear_leaf:
    quest_type = "Main"


# Lookup table
QUEST_TABLE = {
    'get_leaf': get_clear_leaf
}
