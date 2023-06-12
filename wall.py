
import utils 
from snake_types import Loc


class Wall:
    def __init__(self, location:Loc,direction:str,length:int=3)-> None:
        """
        creates new wall
        """
        #location is the middle, move
        self.middle:Loc=location
        self.dir:str=direction
        #if the length is even the middle will be the
        #upper one, for example [(),(),(middle),()]
        self.length=length
    
  
    def change_dir(self):
        """
        changes the direction of the wall
        """
        self.dir=utils.opposite_direction(self.dir)
    
    def move_wall(self,times:int=1)->None:
        """move the wall to the current direction"""
        for _ in range(times):
            self.__move_wall_one()
    
    def __move_wall_one(self)->None:
        """move the wall one square"""
        self.middle=utils.update_location(self.middle,self.dir)
        
    def get_wall_locations(self)->list[Loc]:
        """return the wall locations"""
        locations=[self.middle]

        self.__from_middle(locations)
        self.__before_middle(locations)
        
        return locations

    def __from_middle(self,locations:list):
        half_length = self.length // 2
        even = self.length%2
        from_middle=half_length-1+even
        
        loc = self.middle
        for _ in range(from_middle):   
            loc = utils.update_location(loc, self.dir)
            locations.insert(0, loc)
            
    def __before_middle(self,locations:list):
            half_length = self.length // 2          
            loc=self.middle
            dir=utils.opposite_direction(self.dir)
            for _ in range(half_length):   
                loc=utils.update_location(loc,dir)
                locations.append(loc)
        
    def is_wall(self,loc:Loc)->bool:
        locations=self.get_wall_locations()
        return loc in locations
    
    def get_head(self)->Loc:
        """
        return the head of the wall,(based on his direction)
        """
        locations=self.get_wall_locations()
        if len(locations) == 0:
            return None
        return locations[0] 

        


