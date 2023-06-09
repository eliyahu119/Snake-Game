

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"


class Snake:

    def __init__(self, started_pos:tuple[int,int], dir:str,length:int=3) -> None:
        # self.snake=[(x,y),(x1,y1),(x2,y2)]
        pass

    def add_length(self, x):
        """
            add the new length to the snake 
            return the new length
        """
        pass

    def cut_snake(self, pos: tuple[int, int]) -> None:
        """cut the snake in a certain pos"""
        #please consider whats happening when the length is 1
        #remove the
        pass

    def get_snake_positions(self) -> list[tuple[int, int]]:
        """return all the snake current pos """
        # TODO: return a list of tuples of positions.
        pass

    def change_dir(self, direction: str) -> bool:
        """change directions, return True if succeeded"""

        # TODO: please notice the bs they wrote about changing direction
        # (if its up it cannot got down etc...)
        pass

    def move_snake(self, time_to_move: int=1) -> None:
        """update the snake positions"""
        for _ in range(time_to_move):
            self.__move_snake_one()

    def __move_snake_one() -> None:
        # change the loc of the tail to the current head
        #
        pass

    def is_part_of_snake(loc: tuple[int, int]) -> bool:
        """return if a location is part of the snake"""
        pass

    def get_head()->tuple[int,int]:
        """return the position of the head"""
        pass
    
    def check_if_hit_himself()->bool:
        pass
    
    def reset_snake():
        pass
