class Stamina:
    max_stamina = 20

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


class Inventory:
    inv = []
    max_storage = 9
