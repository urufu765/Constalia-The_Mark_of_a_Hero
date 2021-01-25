"""
The main source for most of the texts all gathered here
"""


class action_text:
    invalid_action = ""
    invalid_input = "Invalid input!"
    valid_action = ""
    run_into_solid = "There's something in the way!"
    move_action = "You moved!"
    door_locked = "Door's locked!"
    to_new_area = "You exited {}"
    ask_sleeping = "Would you like to go to sleep and recover stamina?[Y/N]\n"
    done_sleeping = "You feel refreshed and ready to tackle the world!"


class placeholder:
    placeholder_sign = "Sign here!"


class system_text:
    """System messages"""
    text = (
        "\n  vvvvvvvvv"
        "\n> Caution!! <"
        "\n  ^^^^^^^^^\n"
        "\nThis game is built with the font 'Consolas' in mind. Without it can"
        " cause some missing textures and weird visuals"
        "\nproblems. If 'Consolas' is unavailable, try to find a suitable"
        " monospaced font that works the best.\n"
        "\nTest: |ﬓﬔﬕﬖ█▓▒░■□|Ξ‼⌠⌡╭╮╰╯─│|┌┐└┘├┤┬┴┼╌|═║╔╗╚╝╟╠╢╣|╧╩╬╞╡━┃┏┓┗|"
        "┛┣┫┳┻╋ḻᶸλɅ|‗ᴜ≥ꞈ╷╴҈|"
        "\n      |^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^"
        "^^^^^|^^^^^^^|\n"
        "\nCheck that each character aligns with each arrow,"
        "\nand the top vertical lines aligns with the bottom vertical lines."
        "\nif any of these characters appear as question mark,"
        "\nor the characters don't align with the arrow, please use a"
        " different font"
        "\nIf everything looks okay, then..."
        "\n⌠Press enter to continue...⌡")
    controls = (
        "╭─────────────────────────────────────────────────────────────╮\n"
        "│System Message: There are four control schemes               │\n"
        "│that you can choose from.                                    │\n"
        "├─────────────────────────────────────────────────────────────┤\n"
        "│Please select from one of the four listed:                   │\n"
        "├─────────────────────────────────────────────────────────────┤\n"
        "│          UP   ╷ DOWN  ╷ LEFT  ╷ RIGHT ╷ QUEST  ╷ INVENTORY  │\n"
        "├─┬─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
        "│1│NSWE: (N)orth│(S)outh│(W)est │(E)ast │(Q)uest │(I)nventory │\n"
        "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
        "│2│UDLR: (U)p   │(D)own │(L)eft │(R)ight│(Q)uest │(I)nventory │\n"
        "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
        "│3│WSAD: (W)    │(S)    │(A)    │(D)    │(Q)     │(E)         │\n"
        "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
        "│4│NUMP: (8)    │(2),(5)│(4)    │(6)    │(*)     │(/)         │\n"
        "╰─┴─────────────┴───────┴───────┴───────┴────────┴────────────╯\n")


class quest_text:
    quest_fin = "You completed '{}'"  # add name
    quest_accept = "Accept quest?[y/n]"
    quest_Start = (
        "You got a new quest! You can view your quest log by pressing {}!"
        # add key layout in main program
        )
    q0001 = "Get 'Clear Leaf' from Ravia"


class item_text:
    i0000 = "You got an item! You can view your items by pressing {}!"
    i0001 = "Clear Leaf"
    i0002 = "Blunt Stick"
