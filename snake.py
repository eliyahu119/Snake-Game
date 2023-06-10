

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"


class Snake:

    def __init__(self, started_pos: tuple[int, int]) -> None:
        x = started_pos[0]
        y = started_pos[1]
        self.snake = [(x, y), (x, y-1), (x, y-1)]
        self.pre_dir = "Up"
        self.cur_dir = "Up"

    def add_length(self, snake: list[tuple[int, int]], cur_dir: str):
        """
            enlarges the size of the snake by 1
            updates the snake length
        """
        updated_snake = self.snake
        x_head = snake.get_head(self.snake)[0]
        y_head = snake.get_head(self.snake)[1]
        if cur_dir == 'Left':
            updated_snake.insert(0, (x_head-1, y_head)
        elif cur_dir == 'Right':
            updated_snake.insert(0, (x_head + 1, y_head))
        elif cur_dir == 'Up':
            updated_snake.insert(0, (x_head, y_head+1))
        elif cur_dir == 'Down':
            updated_snake.insert(0, (x_head, y_head - 1))
        self.snake = updated_snake

    def cut_snake(self, pos: tuple[int, int]) -> None:
        """cut the snake in a certain pos"""
        #please consider whats happening when the length is 1
        #remove the
        pass

    def get_snake_positions(self) -> list[tuple[int, int]]:
        """return the entire list of tuples representing the snake current pos"""
        return self.snake

    def change_dir(self, pre_dir: str, cur_dir: str) -> bool:
        """checks if direction is allowed
        return True if it's allowed to turn that way and also updates cur and pre dir"""
        clicked = game_display.get_key_clicked
        if clicked == "Left" and pre_dir != "Right":
            self.pre_dir = self.cur_dir
            self.cur_dir = clicked
            return True
        elif clicked == "Right" and pre_dir != "Left":
            self.pre_dir = self.cur_dir
            self.cur_dir = clicked
            return True
        elif clicked == "Up" and pre_dir != "Down":
            self.pre_dir = self.cur_dir
            self.cur_dir = clicked
            return True
        elif clicked == "Down" and pre_dir != "Up":
            self.pre_dir = self.cur_dir
            self.cur_dir = clicked
            return True
        else:
            return False

    def move_snake(self, time_to_move: int=1) -> None:
        """update the snake positions"""
        for _ in range(time_to_move):
            self.__move_snake_one()

    def __move_snake_one(self, snake: list[tuple[int, int]], pre_dir, cur_dir) -> None:
        """
        if the dir allowed it will move snake to this dir
        updates the snake
        """
        if snake.change_dir(self, pre_dir, cur_dir):
            snake.add_length(self, snake, cur_dir)
            self.snake.pop()
        else:
            return

    def is_part_of_snake(self, loc: tuple[int, int]) -> bool:
        """checks if a location is part of the snake
        True - it's part of the snake or False if it's not"""
        if loc in self.snake:
            return True
        else:
            return False

    def get_head(self, snake: list[tuple])->tuple[int,int]:
        """return the position of the head"""
        return snake[0]
    
    def check_if_hit_himself()->bool:
        pass
    
    def reset_snake():
        pass
