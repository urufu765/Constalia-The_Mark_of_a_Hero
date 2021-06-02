# Changalog
### Update a.1.1 *[Mechanics & Assets Alpha]*
  Anything duplicated is now gone *(most legacy, some recent)*, new folders, and replaced audio with different sounds (and smaller files). Changed some code to accomodate for new textures stuff. Oh and also one new texture: the wall.

  - ./
    - game.py
      - Cleaned up imports (removed legacy & stuff)
      - Deleted a bunch of code that belonged to legacy
    - maps.py
      - Gone.
  - ./assets/portraits/
    - Here's where the portraits of the characters will be located, it will be **something**x**something** (haven't decided)
  - ./assets/audio/
    - Replaced the tracks with smaller ones *(except for track 14, which isn't used and probably won't be used for a while so away it goes)*
  - ./assets/textures/
    - Here's where the textures will be located, it will be **something**x**something** (maybe 50x50)
    - Also a texture was added as a test, and it works.
  - ./resources/
    - engine.py
      - Cleaned up imports
      - Added new import for Texture Files
      - Deleted legacy junk
      - Safely added texture rendering thing (if texture doesn't exist, resort to barbaric colors)
    - eventulate.py
      - removed legacy methods of checking.
    - global_dic.py
      - Finally, global_dic is free from imports (it should never import anything)
      - Legacy things went bye bye
      - Updated music file dictionary to match track names better
      - Removed legacy color dictionary, added brand-spankin'-new texture files dictionary.
      - Changed some map key names.
    - jukebox.py
      - not much here, just placed a TODO to do some error checking just in case.
    - mapper.py
      - Added grass to one of the maps. Now the ground of Mithavil is propery green rather than grey.
      - Some edits here and there, and a TODO to remind myself to remove the hard-coded character drawing coordinates.

---

# Version History
## Version 0: Recode Stage
   Version 0 is all about recoding everything I had done so far in my old project and improve upon it. Stability isn't guaranteed and saves may not work from one version to another.
  ### 0.1 - Essentials recoded
   **(0.1.0)** First playable and downloadable version

   **(0.1.1)** Rearranged code and redid controls(along with adding North South East West)

   **(0.1.2)** Rearranged files to make what the user needs to open very clear and made some changes to the chars

   **(0.1.3)** Added the remaining two control schemes and added quit option, along with fixing a visual aspect of choosing controls and telling the player what the controls are.

  ### 0.2 - Mechanics recoded
   **(0.2.0)** Stamina mechanic added for future use and added door mechanics

   **(0.2.1)** Better implementation of door mechanics to save headache for later

   **(0.2.2)** Implemented bed and relocated a function for cleaner area

   **(0.2.3)** Beds now recover stamina, once stamina is fully implemented, and code has been changed slightly

   **(0.2.4)** Made code less break-y(in terms of keywords), reflowed text for style purposes, and set up a roadmap

  ### 0.3 - Interactables recoded
   **(0.3.0)** Characters can now be talked to, and there is now a "reward" for slamming into a table(hint: it's more dialogue)

   **(0.3.1)** QoL update, no need to press enter now for movement and some other interaction(s)

   **(0.3.2)** Control update: controls now usable with new QoL update and packaged all this into an EXE

   **(0.3.4)** Minor update to include the caution page that warns about fonts.

   **(0.3.5)** Minor/Major internal change that allows save function to work in the future implementations and use of function dictionaries

   **(0.3.6)** Fixed problem where saves don't work as they should

   **[(0.3.7)](https://github.com/urufu765/Constalia-The_Mark_of_a_Hero/releases/tag/(0.3.7))** Rivers and lakes are interactable, signs have placeholders, wheat, and locked doors say stuff

   **[(0.3.8)](https://github.com/urufu765/Constalia-The_Mark_of_a_Hero/releases/tag/(0.3.8))** Just contains new comments to make navigating the code a little easier. Also changed the numpad controls a little bit to make it a bit more convenient

  ### 0.4 - Quests recoded
   **(0.4.0)** First quest somewhat implemented(should be in working order). Save function not tested but should still work as intended. Previous saves from (0.3 m)ay not work. Also hey! I'm starting to get how to use classes and stuff. And also a more detailed update from now on because yes.

   **(0.4.1)** Tested version. Fixed loading issue. The quest is completeable and can be saved and loaded at any time. Added Nyafim, my new rudamentary playtesting assistants.

   **[(0.4.2)](https://github.com/urufu765/Constalia-The_Mark_of_a_Hero/releases/tag/(0.4.2))** Finished up the quest(with some missing parts that will be added in the items update) and added a way to view the current quest. Docstrings have been added where appropriate. Likely the last version of (0.4

## a for alpha: Redoing yet again but with Pygame
   Alpha is basically redoing what I recoded again to fit pygame better because I believe the pygame is the way forward... but if the demand is there I'll update the legacy too
  ### a.0 - Alpha Zero
   *Cleanup never, Pygame: The game first*

   **(a.0.0)** Pygame conversion has started, and the current code has been edited for easy removal once pygame is fully integrated.

   **(a.0.0.1)** No visually noticeable update, but pygame window opens successfully now. Legacy is still on as pygame has yet to be utilized to playable level. At least the game may be playable with legacy on. Hopefully final version where legacy is forced on.

   **(a.0.1)** Say goodbye to Legacy mode. You can only access Legacy by either not having pygame or disabling it in code. The game should function almost exactly like before except you still gotta answer to the terminal. That'll be fixed shortly. Also some colors have been combined for convenience so things may not look as they should, at least for now.

   **(a.0.1.1)** Changed how the changealog looks and changed the version numbering.

  ### a.1 - Mechanics & Assets Alpha
   *Goodbye Legacy, Hello Pygame:*

   **(a.1.0)** Legacy mode has been made obsolete, which means legacy mode will no longer work from here on out *(legacy components will be removed slowly from this point)*. A new way for maps to be loaded has been made and bunch of things were changed to accomodate it. Mithavil has been redone. Music has been added to the game, enjoy the low quality mono track songs. Quests are also unavailable for now due to how maps work. The game is a little unstable at the moment due to many open ends. Also, the version type formatting has changed a little, now it's !->u->s->r, from least stable to most. The update is now visible in README. **And more...**

   **(a.1.0.1)** Hotfix: changed how Changalog looks again

   **(a.1.0.2)** Another one where Changalog is changed a little

   **(a.1.1)** Anything duplicated is now gone *(most legacy, some recent)*, new folders, and replaced audio with different sounds (and smaller files). Changed some code to accomodate for new textures stuff. Oh and also one new texture: the wall.

   **(a.1.1.1)** Forgot to update README.md

---

## Upcoming:
 - Code cleanup
 - Complete removal of legacy
 - Sprites
 - Dialogue boxes
 - Title screen
 - Quests will be able to be switched from active to incomplete.
 - Text renovation.
 - Change how events are loaded in, with a temporary dictionary that loads the events in that area, an appendable dictionary that is loaded first (that is used to store changes in save files), and default set values that are loaded from the map if it doesn't exist in the stored appendable dictionary.
 - New save mechanic that uses class structure (but not classes themselves)
 - Settings

# Roadmap:
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
