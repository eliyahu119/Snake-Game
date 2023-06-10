from snake_types import Loc

LEFT = "left"
RIGHT = "right"
DOWN = "down"
UP = "up"


def update_location(loc:Loc,direction:str)->Loc:
    """
    Update the current location based on the specified direction.

    Args:
        loc (tuple[int,int]): The current (x,y)-coordinates.
        direction (str): The direction to move the location. Must be one of "left", "right", "up", or "down".

    Returns:
        tuple: The updated (x, y) coordinates.
    """
    x,y=loc
    if direction == LEFT:
        return x - 1, y
    elif direction == RIGHT:
        return x + 1, y
    elif direction == UP:
        return x, y + 1
    elif direction == DOWN:
        return x, y - 1
    else:
       return x,y
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

    
    
