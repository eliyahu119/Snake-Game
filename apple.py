import game_utils

class Apple:
    
    def __init__(self,number_of_apples,banned_locations:list[tuple[int,int]]) -> None:
        
        self.apples:set[tuple[int,int]]=[]
        self.__init_apples(number_of_apples,banned_locations)
    
    def __init_apples(self,number_of_apples,banned_locations):   
        for _ in number_of_apples:
            self.add_apple(banned_locations)
    
    def get_apples_loc(self)->set[tuple[int,int]]:
        #return all the apple locations.
        return set(self.apples)
    
    def is_apple(self,apple:tuple[int,int])->bool:
        return apple in self.apples

    def remove_apple(self,loc:tuple[int,int])->bool:
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
        
    def add_apple(self,banned_locations):
        apple=game_utils.get_random_apple_data()
        if apple not in banned_locations:
            self.apples.add(apple)
       
    
    
