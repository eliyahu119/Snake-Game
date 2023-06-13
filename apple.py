import game_utils
from snake_types import Loc


class Apple:

    def __init__(self, apple_locs: list[Loc] = []) -> None:
        """
        creates new apple and updates the set
        """
        self.apples: set[tuple[int, int]] = set(apple_locs)

    def get_apples_loc(self) -> set[Loc]:
        """
        returns a set of all the apple's locations
        """
        return set(self.apples)

    def is_apple(self, apple: Loc) -> bool:
        """
        checks if a given location contains an apple. returns True or False accordingly
        """
        return apple in self.apples

    def remove_apple(self, loc: Loc) -> bool:
        """
        Removes an apple from a specific location.

        Args:
            loc: A tuple representing the coordinates of the location where the apple is located.

        Returns:
            bool: True if the apple was successfully removed, False otherwise.
        """
        try:
            self.apples.remove(loc)
            return True
        except Exception:
            return False

    def add_apple(self, apple: Loc) -> bool:
        """
        tries to add an apple
        if there is already another apple there it will only return False
        otherwise it adds it and returns True
        """
        if apple in self.apples:
            return False
        else:
            self.apples.add(apple)
            return True
