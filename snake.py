import utils


class Snake:

    def __init__(self, started_pos: tuple[int, int], direction: str = utils.UP) -> None:
        """
        creates new snake by resetting
        """
        self.reset_snake(started_pos, direction)

    def add_length(self):
        """
            enlarges the size of the snake by 1
            updates the snake length
        """
        head = self.get_head()
        update = utils.update_location(head, direction=self.direction)
        self.snake.insert(0, update)

    def cut_snake(self, pos: tuple[int, int]) -> None:
        """cut the snake in a certain pos, unless it's cut only the head"""
        if pos == self.get_head():
            return
        if pos not in self.snake:
            return
        index = self.snake.index(pos)
        self.snake = self.snake[:index]

    def get_snake_positions(self) -> list[tuple[int, int]]:
        """return the entire list of tuples representing the snake current pos"""
        return list(self.snake)

    def change_dir(self, direction: str) -> bool:
        """update direction if allowed, returns True if succeeded and False if not"""
        if self.direction != utils.opposite_direction(direction):
            self.direction = direction
            return True
        else:
            return False

    def move_snake(self, time_to_move: int = 1) -> None:
        """update the snake positions"""
        for _ in range(time_to_move):
            self.__move_snake_one()

    def __move_snake_one(self) -> None:
        """
        move snake to this direction by 1 place - updates the snake
        """
        self.add_length()
        self.snake.pop()

    def is_part_of_snake(self, loc: tuple[int, int]) -> bool:
        """checks if a location is part of the snake
        True - it's part of the snake or False if it's not"""
        if loc in self.snake:
            return True
        else:
            return False

    def get_head(self) -> tuple[int, int]:
        """returns the position of the head"""
        return self.snake[0]

    def check_if_hit_itself(self) -> bool:
        """
        checks if the snake hit itself
        returns True if it did or False otherwise
        """
        if self.snake.count(self.get_head()) > 1:
            return True
        else:
            return False

    def reset_snake(self, started_pos: tuple[int, int], direction=utils.UP):
        """
        reset the snake completely: location, length and direction
        """
        snake = [started_pos]
        opp_dir = utils.opposite_direction(direction)
        pos = started_pos
        for _ in range(2):
            pos = utils.update_location(pos, opp_dir)
            snake.append(pos)
        self.snake = snake
        self.direction = direction

    # def _reset_pos(started_pos):
