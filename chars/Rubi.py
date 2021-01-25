class expressions:
    """facial expression"""
    # normal
    e000 = ("\n╭─────╮"
            "\n│λꞈꞈλ │"
            "\n│ | |ꞈ│"
            "\n│  ꞈꞈ/├────────────────────────────────╮"
            "\n│   \ │ Rubi                           │")
    # happy
    e001 = ("\n╭─────╮"
            "\n│λꞈꞈλ │"
            "\n│ ᴖ ᴖꞈ│"
            "\n│  ꞈꞈ/├────────────────────────────────╮"
            "\n│   \ │ Rubi                           │")
    # slightly confused
    e002 = ("\n╭─────╮"
            "\n│λꞈꞈλ │"
            "\n│ ᴛ |ꞈ│"
            "\n│  ꞈꞈ/├────────────────────────────────╮"
            "\n│   \ │ Rubi                           │")
    # irritated
    e003 = ("\n╭─────╮"
            "\n│λꞈꞈλ │"
            "\n│ ᴛ ᴛꞈ│"
            "\n│  ꞈꞈ/├────────────────────────────────╮"
            "\n│   \ │ Rubi                           │")
    # meh
    e004 = ("\n╭─────╮"
            "\n│λꞈꞈλ │"
            "\n│ - -ꞈ│"
            "\n│  ꞈꞈ/├────────────────────────────────╮"
            "\n│   \ │ Rubi                           │")


class talking:
    """Talking"""
    # interacting with Firay in home
    # giving quest
    t000 = ("├─────┴────────────────────────────────┤"
            "\n│ Good morning~                        │"
            "\n│ Had a good night sleep?              │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t001 = ("├─────┴────────────────────────────────┤"
            "\n│ Lovely~                              │"
            "\n│ Now off with ya!                     │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t002 = ("├─────┴────────────────────────────────┤"
            "\n│ ...!                                 │"
            "\n│ Wait!                                │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t003 = ("├─────┴────────────────────────────────┤"
            "\n│ Could you get me a clear leaf for    │"
            "\n│ me? I think Raiva has some to spare. │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t004 = ("├─────┴────────────────────────────────┤"
            "\n│ Her house should be the first house  │"
            "\n│ across the river...                  │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t005 = ("├─────┴────────────────────────────────┤"
            "\n│ That is if she hasn't moved again    │"
            "\n│ because her house is 'haunted with   │"
            "\n│ ghosts of wind'...                   │"
            "\n└────────────────┤....├────────────────┘")
    t006 = ("├─────┴────────────────────────────────┤"
            "\n│ Whatever that means..                │"
            "\n│ Now off you go!                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    t007 = ("├─────┴────────────────────────────────┤"
            "\n│ Lovely day, ain't it?                │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    # ending quest
    t008 = ("├─────┴────────────────────────────────┤"
            "\n│ It's the most essential ingredient   │"
            "\n│ that I need to make the              │"
            "\n│ 'Spirit page'.                       │"
            "\n└────────────────┤....├────────────────┘")
    t009 = ("├─────┴────────────────────────────────┤"
            "\n│ It's a piece of paper that,          │"
            "\n│ according to the legends, stores the │"
            "\n│ spirit of the user.                  │"
            "\n└────────────────┤....├────────────────┘")
    t010 = ("├─────┴────────────────────────────────┤"
            "\n│ But so far, nobody has been able to  │"
            "\n│ use this piece of paper.             │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t011 = ("├─────┴────────────────────────────────┤"
            "\n│ Supposedly, no one but the           │"
            "\n│ Riaceovians can use the 'Spirit-     │"
            "\n│ page'...                             │"
            "\n└────────────────┤....├────────────────┘")
    t012 = ("├─────┴────────────────────────────────┤"
            "\n│ But Riaceovians had disappeared a    │"
            "\n│ long time ago...                     │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t013 = ("├─────┴────────────────────────────────┤"
            "\n│ .....                                │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t014 = ("├─────┴────────────────────────────────┤"
            "\n│ I should start putting the materials │"
            "\n│ together... would you mind playing   │"
            "\n│ outside just for a while?            │"
            "\n└────────────────┤....├────────────────┘")


class Rubi:
    NAME = 'Rubi'
    TYPE = 'NPC'
    EXPR = expressions()
    TALK = talking()
