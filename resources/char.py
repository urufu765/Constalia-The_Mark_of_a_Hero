"""
Everything that concerns with characters.
"""
from typing import List


class Thing:  # Placeholder
    x: int
    y: int
    type: str  # to be used later when sprites are a thing

    def __init__(self, x: int, y: int, type: str) -> None:
        self.x, self.y, self.type = x, y, type


class Player(Thing):  # Placeholder
    inv: List[any]
    max_stamina = 20
    max_storage = 9

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 'firay')
        self.inv = []

    def stamina_recovery(self, current: int, type: str) -> int:
        """
        Function for recovering stamina depending on the source
        """
        if type == 'bed':
            return self.max_stamina
        return current

    def stamina_check(current: int) -> bool:
        """
        Checks whether there is stamina
        """
        if current < 1:
            return False
        return True


class Characters(Thing):  # Placeholder
    name: str

    def __init__(self, x: int, y: int, name: str) -> None:
        super().__init__(x, y, 'npc')
        self.name = name
