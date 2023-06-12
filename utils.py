from snake_types import Loc

LEFT = "Left"
RIGHT = "Right"
DOWN = "Down"
UP = "Up"

BLUE = "blue"
BLACK = "black"
GREEN = "green"

def update_location(loc: Loc, direction: str) -> Loc:
    """
    Update the current location based on the specified direction.

    Args:
        loc (tuple[int,int]): The current (x,y)-coordinates.
        direction (str): The direction to move the location. Must be one of "left", "right", "up", or "down".

    Returns:
        tuple: The updated (x, y) coordinates.
    """
    row, col = loc
    if direction == LEFT:
        return row-1, col
    elif direction == RIGHT:
        return row+1, col
    elif direction == UP:
        return row, col+1
    elif direction == DOWN:
        return row, col-1
    else:
        return row, col
        # raise ValueError("Invalid direction. Please provide one of 'left', 'right', 'up', or 'down'.")


def opposite_direction(direction):
    if direction == UP:
        return DOWN
    elif direction == DOWN:
        return UP
    elif direction == LEFT:
        return RIGHT
    elif direction == RIGHT:
        return LEFT
    else:
        return direction
    # raise ValueError("Invalid direction. Please provide one of the valid directions.")
