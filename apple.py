import game_utils
from snake_types import Loc

class Apple:
    
    def __init__(self,apple_locs:list[Loc]=[]) -> None:
        self.apples:set[tuple[int,int]]=set(apple_locs)
    
    def get_apples_loc(self)->set[Loc]:
        #return all the apple locations.
        return set(self.apples)
    
    def is_apple(self,apple:Loc)->bool:
        return apple in self.apples

    def remove_apple(self,loc:Loc)->bool:
        """
        Removes an apple from a specified location.

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
        
    def add_apple(self,apple:Loc)->bool:
        if apple in self.apples:
            return False
        return self.apples.add(apple)

    
    
    
