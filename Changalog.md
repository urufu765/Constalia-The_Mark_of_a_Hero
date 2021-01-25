# Changalog
## Version 0.1~0.5 - "Recode-stage"
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

 - global_dic.py
    - Removed unused quests import as it was causing circular import error.
    - Changed Rubi's interactable status from False to True
    - Updated quests dictionary layout

 - eventulate.py
    - Added new import to use the function run_quest from quests.py
    - Edited char_check function appropriately
    - Clarified a little what the character function in the apply_interactions class should do

 - Rubi.py
    - Removed all the pesky \n that should've been yeeted in one of the previvous updates.(may add it all back later idk)

 - texts.py
    - quest_accept text added

 - quests.py
    - Almost everything has been changed and added.

## Upcoming:
 The first quest will be better implemented, and the code should look a little cleaner after some renovations(may not happen). Also doctext or whatever will be added to where appropriate.

# Roadmap:
### 0.5: The end of recoded, with addons(will include new map)
 Tying up loose ends, finishing incomplete features, adding new contents. Guaranteed new map.
### 0.6: Party Update
 All about recruiting and stat checking!
### 0.7: Combat Update
 All about combat! This update is gonna be big.