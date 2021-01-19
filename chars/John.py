class expressions:
    """Facial expressions"""
    e000 = ("\n╭─────╮"
            "\n│Aꞈ_A │"
            "\n│ | |‗│"
            "\n│  __/├────────────────────────────────╮"
            "\n│   \ │ John                           │")
    e001 = ("\n╭─────╮"
            "\n│Aꞈ_A │"
            "\n│ - -‗│"
            "\n│  __/├────────────────────────────────╮"
            "\n│   \ │ John                           │")


class talking:
    """Talking"""
    t000 = ("├─────┴────────────────────────────────┤"
            "\n│ ...                                  │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t001 = ("├─────┴────────────────────────────────┤"
            "\n│ ....                                 │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")


class JOHN:
    NAME = 'John'
    TYPE = 'ALLY'
    EXPR = expressions()
    TALK = talking()
