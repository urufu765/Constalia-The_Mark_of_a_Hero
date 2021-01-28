"""
For saving and loading.
"""
from typing import List
from resources.global_dic import variables as DV
from resources.global_dic import doors as DD
from resources.global_dic import interactables as DI
from resources.global_dic import quests as DQ
import assets.texts as t
from os import path
import sys


Nyafim = False


def file_path_finder() -> str:
    """
    Finds the path that contains the saving folder.
    """
    if path.exists(path.expanduser('~\\Documents\\TMoaH')):
        return '\\Documents'
    elif path.exists(path.expanduser('~\\Downloads\\TMoaH')):
        return '\\Downloads'
    return ''


def get_resource_path(relative_path):
    """
    Gets the relative filepath
    """
    try:
        base_path = path.expanduser('~{}\\TMoaH'.format(file_path_finder()))
    except Exception:
        base_path = sys._MEIPASS
        print("Unknown error occured, you will be unable to save.")
    return path.join(base_path, relative_path)


def convertor(array: str) -> List[object]:
    """
    Converts strings in the list to correct types
    """
    temp_array = []
    an_array = array.strip('][').split(', ')
    if Nyafim:
        print(f"<Here's the array in question: {an_array}>")
    for x in an_array:
        if x.isnumeric():
            if Nyafim:
                print(f"<{x} is numeric>")
            temp_array.append(int(x))
        elif x == 'True':
            if Nyafim:
                print(f"<{x} is True>")
            temp_array.append(True)
        elif x == 'False':
            if Nyafim:
                print(f"<{x} is False>")
            temp_array.append(False)
        else:
            if Nyafim:
                print(f"<{x} is string>")
            temp_array.append(x.strip("'").strip('"'))
    if Nyafim:
        print(f'<Here! {temp_array}>')
    return temp_array


def quest_convertor(array: str) -> List[object]:
    """
    Converts strings in the list to correct types. Specialized for quests.
    """
    temp_array = []
    temp_array_2 = []
    an_array = array[1:-1].split(', ')
    if Nyafim:
        print(f"<Here's the array in question: {an_array}>")
    for x in an_array:
        if x.isnumeric():
            if Nyafim:
                print(f"<{x} is numeric>")
            temp_array.append(int(x))
        elif x == 'True':
            if Nyafim:
                print(f"<{x} is True>")
            temp_array.append(True)
        elif x == 'False':
            if Nyafim:
                print(f"<{x} is False>")
            temp_array.append(False)
        elif len(temp_array) >= 2:
            if Nyafim:
                print(f"<{x} is part of an array>")
            temp_array_2.append(x.strip('][').strip("'").strip('"'))
        else:
            if Nyafim:
                print(f"<{x} is string>")
            temp_array.append(x.strip("'").strip('"'))
    temp_array.append(temp_array_2)
    if Nyafim:
        print(f'<Here! {temp_array}>')
    return temp_array


def save_game() -> None:
    """
    Saves the game to the desired slot
    """
    checked_save = False
    desired_num = '0'
    while not checked_save:
        desired_num = input("Save to slot: ")
        if desired_num.isdigit():
            checked_save = True
        else:
            print(t.action_text().invalid_input)
            print("Numbers only!")
    destination = get_resource_path('saves\\save_{}'.format(desired_num))
    # destination = 'saves\\save_{}'.format(desired_num)  # legacy
    if Nyafim:
        print(f"<Destination is {destination}>")
    with open(destination, 'w') as file:
        for x in DV:  # Global dictionary
            file.write(x + ';' + str(DV[x]) + '\n')
        file.write("END\n")
        for d in DD:  # Door dictionary
            file.write(d + ';' + str(DD[d]) + '\n')
        file.write("END\n")
        for i in DI:  # Item dictionary
            file.write(i + ';' + str(DI[i]) + '\n')
        file.write("END\n")
        for q in DQ:  # Quest dictionary
            file.write(q + ';' + str(DQ[q]) + '\n')
        file.write("END\n")
    print("Successfully saved to save_{}".format(desired_num))


def load_game() -> None:
    """
    Loads the game from the desired slot
    """
    checked_load = False
    desired_num = '0'
    while not checked_load:
        desired_num = input("Load from slot: ")
        if desired_num.isdigit():
            checked_load = True
        else:
            print(t.action_text().invalid_input)
            print("Numbers only!")
    destination = get_resource_path('saves\\save_{}'.format(desired_num))
    if Nyafim:
        print(f"<Destination is {destination}>")
    # destination = 'saves\\save_{}'.format(desired_num)  # legacy
    try:
        with open(destination) as file:
            location_index = {
                'main': DV,
                'doors': DD,
                'interactables': DI,
                'quests': DQ
            }
            modes = ['main', 'doors', 'interactables', 'quests', 'spacer']
            num = 0
            for w in location_index:
                while w == modes[num]:
                    x = file.readline()
                    if x.strip('\n') == 'END':  # mode changer
                        num += 1
                    else:
                        y = x.split(';')
                        z = y[1].strip('\n')
                        if z.isnumeric():
                            location_index[w][y[0]] = int(z)
                        elif modes[num] == 'quests':
                            location_index[w][y[0]] = quest_convertor(z)
                        elif modes[num] != 'main':
                            location_index[w][y[0]] = convertor(z)
                        else:
                            location_index[w][y[0]] = z
        print("Successfully loaded save from save_{}".format(desired_num))
    except IOError:
        print("Error loading file")
