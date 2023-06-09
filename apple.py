import game_utils

class Apple:
    
    def __init__(self,number_of_apples) -> None:
        self.__init_apples(number_of_apples)
    
    def __init_apples(self,number_of_apples):   
        # game_utils.get_random_apple_data()
        pass
    
    def get_apples_loc()->list[tuple[int,int]]:
        #return all the apple locations.
        pass
    
    def is_apple(loc:tuple[int,int])->bool:
        pass
    
    def remove_apple(loc:tuple[int,int])->bool:
        """
        Removes an apple from a specified location.

        Args:
            loc: A tuple representing the coordinates of the location where the apple is located.

        Returns:
            bool: True if the apple was successfully removed, False otherwise.
        """
        pass
    
    
    
