from typing import Optional
from game_display import GameDisplay
from snake import Snake
from wall import Wall
from apple import Apple
import utils


class SnakeGame:

    def __init__(self, args) -> None:
        self.args = args
        started_pos=args.width //2,args.height //2 
        self.__key_clicked = None
        self.__snake = Snake(started_pos)
        self.__snake.add_length()
        self.__snake.add_length()
        
        # self.apple = Apple
        # self.wall: list[Wall] = []

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        self.change_dir_objects()
        self.move_objects()

    def change_dir_objects(self):
        self.__snake_change_dir()
        # self.__walls_change_dir()

    def move_objects(self):
        # self.__move_walls()
        self.__move_snake()

    def __snake_change_dir(self):
        if self.__key_clicked is not None:
            self.__snake.change_dir(self.__key_clicked)

    def __move_snake(self):
        self.__snake.move_snake()

    # def __move_walls():
    #     pass

    def draw_board(self, gd: GameDisplay) -> None:
        self. __draw_snake(gd)
        # gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        in_bound=self.check_head_in_bound()
        if not in_bound:
            return True
        hit_himself=self.__snake.check_if_hit_itself()
        if hit_himself:
            return True
         

        
    def check_head_in_bound(self):
        head=self.__snake.get_head()
        return self.in_bound(head)
        
    def in_bound(self, loc: tuple[int, int]) -> bool:
        x, y = loc
        if not (0 <= x < self.args.width):
            return False
        if not (0 <= y < self.args.height):
            return False
        return True

    def __draw_snake(self, gd: GameDisplay) -> None:
        bla=True
        for loc in self.__snake.get_snake_positions():
            if self.in_bound(loc):
                self._x, self._y = loc
                if bla: #TODO DELETE BLA
                    gd.draw_cell(self._x, self._y, utils.BLACK)
                else:                          
                    gd.draw_cell(self._x, self._y, utils.GREEN)
                bla = not bla
