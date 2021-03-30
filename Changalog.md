# Changalog
### Update a.0.1.1n <Alpha 0>
  Changed how the changealog looks and changed the version numbering.


# Version History
## Version 0: Recode Stage
    Version 0 is all about recoding everything I had done so far in my old project and improve upon it. Stability isn't guaranteed and saves may not work from one version to another.
  ### 0.1 - Essentials recoded
    0.1.0: First playable and downloadable version

    0.1.1: Rearranged code and redid controls(along with adding North South East West)

    0.1.2: Rearranged files to make what the user needs to open very clear and made some changes to the chars

    0.1.3: Added the remaining two control schemes and added quit option, along with fixing a visual aspect of choosing controls and telling the player what the controls are.

  ### 0.2 - Mechanics recoded
    0.2.0: Stamina mechanic added for future use and added door mechanics

    0.2.1: Better implementation of door mechanics to save headache for later

    0.2.2: Implemented bed and relocated a function for cleaner area

    0.2.3: Beds now recover stamina, once stamina is fully implemented, and code has been changed slightly

    0.2.4: Made code less break-y(in terms of keywords), reflowed text for style purposes, and set up a roadmap

  ### 0.3: Interactables recoded
    0.3.0: Characters can now be talked to, and there is now a "reward" for slamming into a table(hint: it's more dialogue)

    0.3.1: QoL update, no need to press enter now for movement and some other interaction(s)

    0.3.2: Control update: controls now usable with new QoL update and packaged all this into an EXE

    0.3.4: Minor update to include the caution page that warns about fonts.

    0.3.5: Minor/Major internal change that allows save function to work in the future implementations and use of function dictionaries

    0.3.6: Fixed problem where saves don't work as they should

    0.3.7: Rivers and lakes are interactable, signs have placeholders, wheat, and locked doors say stuff

    0.3.8: Just contains new comments to make navigating the code a little easier. Also changed the numpad controls a little bit to make it a bit more convenient

  ### 0.4: Quests recoded
    0.4.0: First quest somewhat implemented(should be in working order). Save function not tested but should still work as intended. Previous saves from 0.3 may not work. Also hey! I'm starting to get how to use classes and stuff. And also a more detailed update from now on because yes.

    0.4.1: Tested version. Fixed loading issue. The quest is completeable and can be saved and loaded at any time. Added Nyafim, my new rudamentary playtesting assistants.

    0.4.2: Finished up the quest(with some missing parts that will be added in the items update) and added a way to view the current quest. Docstrings have been added where appropriate. Likely the last version of 0.4

## a for alpha: Redoing yet again but with Pygame
    Alpha is basically redoing what I recoded again to fit pygame better because I believe the pygame is the way forward... but if the demand is there I'll update the legacy too
  ### a.0 Cleanup never, Pygame: The game first:
    a.0.0.0: Pygame conversion has started, and the current code has been edited for easy removal once pygame is fully integrated.

    a.0.0.1: No visually noticeable update, but pygame window opens successfully now. Legacy is still on as pygame has yet to be utilized to playable level. At least the game may be playable with legacy on. Hopefully final version where legacy is forced on.

    a.0.1.0: Say goodbye to Legacy mode. You can only access Legacy by either not having pygame or disabling it in code. The game should function almost exactly like before except you still gotta answer to the terminal. That'll be fixed shortly. Also some colors have been combined for convenience so things may not look as they should, at least for now.

    a.0.1.1: Changed how the changealog looks and changed the version numbering.


## Upcoming:
 - Sprites
 - Quests will be able to be switched from active to incomplete.
 - Text renovation.
 - Music. No more silence.
 - Change how events are loaded in, with a temporary dictionary that loads the events in that area, an appendable dictionary that is loaded first (that is used to store changes in save files), and default set values that are loaded from the map if it doesn't exist in the stored appendable dictionary.

# Roadmap:
 ### a.1: Mechanics & Assets Alpha
  Adapting the mechanics fully and completing maps to make pygame work as intended, as well as making new assets and stuff
 ### a.2: Maps Alpha
  Redoing maps to make the game a whole lot better
 ### a.3: Interactables 2.0 Alpha
  Adapting and improving the interactables fully to work better with pygame
 ### a.4: Quests 2.0 Alpha
  Quests. Improve and adapt the old design to fit pygame and such.
 ### b.1: Items Update
  Inventory will actually be a thing.
 ### b.2: Party Update
  All about recruiting and stat checking!
 ### b.3: Combat Update
  All about combat! This update is gonna be big.
