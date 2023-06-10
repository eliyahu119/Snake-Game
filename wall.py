
import utils 


class Wall:
    def __init__(self,location:tuple[int,int],direction:str,length:int=3,)-> None:
        #location is the middle, move
         pass
  
    def change_dir(self):
        pass
    
    def move_wall(self,times:int=1)->None:
        """move the wall to the current direction"""
        for _ in range(times):
            self.__move_wall_one()
    
    def __move_wall_one(self)->None:
        """move the wall one square"""
        pass
        
    def get_wall_locations(self)->list[tuple[int,int]]:
        """return the wall locations"""
        pass 
    
    def is_wall(loc:tuple[int,int])->bool:
        pass
    
    def get_head()->tuple[int,int]:
        """
        return the head of the wall,(based on his direction)
        """
        #for example if the dir is left,up wil return n-1
        #right,down, will return [0]
        pass
