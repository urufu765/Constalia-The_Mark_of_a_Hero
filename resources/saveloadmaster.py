from typing import List
from resources.global_dic import variables as DV
from resources.global_dic import doors as DD
from resources.global_dic import interactables as DI
from resources.global_dic import quests as DQ
import assets.texts as t
from os import path
import sys


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
    for x in an_array:
        if x.isnumeric():
            temp_array.append(int(x))
        elif x == 'True':
            temp_array.append(True)
        elif x == 'False':
            temp_array.append(False)
        else:
            temp_array.append(x.strip("'").strip('"'))
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
    with open(destination, 'w') as file:
        for x in DV:
            file.write(x + ';' + str(DV[x]) + '\n')
        file.write("END\n")
        for d in DD:
            file.write(d + ';' + str(DD[d]) + '\n')
        file.write("END\n")
        for i in DI:
            file.write(i + ';' + str(DI[i]) + '\n')
        file.write("END\n")
        for q in DQ:
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
                    if x.strip('\n') == 'END':
                        num += 1
                    else:
                        y = x.split(';')
                        z = y[1].strip('\n')
                        if z.isnumeric():
                            location_index[w][y[0]] = int(z)
                        elif modes[num] != 'main':
                            location_index[w][y[0]] = convertor(z)
                        else:
                            location_index[w][y[0]] = z
        print("Successfully loaded save from save_{}".format(desired_num))
    except IOError:
        print("Error in loading file")
