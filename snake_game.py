from typing import Optional
from game_display import GameDisplay
from snake import Snake
from wall import Wall
from apple import Apple
import game_utils
import utils


class SnakeGame:
        

        def __init__(self, args) -> None:
            """
            general reset of the game
            """
            self.args = args
            self.__key_clicked = None
            self.round = 0
            self.score = 0
            self.grow = 0
            self.apples_eaten=0            
            
            self.__init_snake()
            self.__init_walls()
            self.__init_apples()
        def __init_apples(self):
            """
            initiate apples list
            """
            self.apples=Apple()
            
        def __add_apples(self):
            """
            adds another apple to their container. returns True if succeeded
            """
            if len(self.apples.get_apples_loc()) >= self.args.apples:
                return False
            apple = game_utils.get_random_apple_data()
            if not self.__check_if_empty(apple):
                return False
            self.apples.add_apple(apple)
            return True
       
        def __check_in_apples(self,loc:set[tuple[int,int]]):
            """
            checks if a location is in the apple's locations list
            """
            apples=self.apples.get_apples_loc()
            return utils.check_if_common_list(loc,apples)
            
        def __draw_apples(self, gd: GameDisplay) -> None:
            """
            draw apples on the board
            """
            positions=self.apples.get_apples_loc() 
            for loc in positions:
                if self.__in_bound(loc):
                    _x, _y = loc
                    gd.draw_cell(_x,_y, utils.GREEN)

        def __init_walls(self):
            """
            initiate wall's list
            """
            self.walls:list[Wall]=[]

        def __add_wall(self):
            """
            add a wall to wall's list
            """
            wall_len=len(self.walls)
            if wall_len >= self.args.walls:
                return False
            wall=self.__get_valid_wall()
            if wall is None:
                return False
            self.walls.append(wall)
            return True
            
        def __get_valid_wall(self):
            x,y,d=game_utils.get_random_wall_data()
            wall=Wall((x,y),d)
            locs=wall.get_wall_locations()
            is_empty=self.__check_if_empty_lst(locs)
            if is_empty:
                return wall
            else:
                return None
                
        def __draw_walls(self,gd):
            """
            draw walls on the board
            """
            flat_walls=self.__get_flat_walls()
            for loc in flat_walls:
                if self.__in_bound(loc):
                    __x, __y = loc
                    gd.draw_cell(__x, __y, utils.BLUE)        
        
        def __get_flat_walls(self):
            flat=[]
            for wall in self.walls:
                flat.extend(wall.get_wall_locations())
            return flat
            # return [loc for wall.get_wall_locations() in self.walls for loc in wall]
        
        def __move_walls(self)->None:
            """
            Moves the walls in the game.

            This is a private method that moves the walls in the game based on the game logic,
            every even round. not including the first one.

            Returns:
                None
            """
            
            
            if self.round == 0 or self.round % 2 == 1:
                return 
            for wall in self.walls:
                wall.move_wall()
        
        def __remove_out_borders_walls(self)->None:
            """
            removes walls that exit borders
            """
            new_arr=[]
            for wall in self.walls:
                pos=wall.get_wall_locations()
                out_border=self.__array_out_bound(pos)
                if not out_border:
                    new_arr.append(wall)
            self.walls=new_arr
        
        def get_heads(self):
            return list(map(lambda x:x.get_head(),self.walls))

        def read_key(self, key_clicked: Optional[str]) -> None:
            """
            updates what the user has clicked
            """
            self.__key_clicked = key_clicked

        def update_objects(self) -> None:
            """
            updates direction and move objects
            """
            self.change_dir_objects()
            self.move_objects()
            
        def change_dir_objects(self):
            """
            changes object's direction
            """
            self.__snake_change_dir()

        def move_objects(self):
            """
            Moves the walls and the snake in the game.

            This function is responsible for moving the walls and the snake in the game.
            It calls private methods __move_walls() and __move_snake() to perform the actual movement.

            Returns:
                None
            """
            self.__move_walls()
            self.__move_snake()

        def draw_board(self, gd: GameDisplay) -> None:
            """
            draws the snake, the walls and the apples
            """
            self. __draw_snake(gd)
            self.__draw_walls(gd)
            self.__draw_apples(gd)

        def check_collisions(self):
            self.__remove_out_borders_walls()
            self.__destroy_apple_in_walls()
            self.__eat_apple()
       
        def end_round(self) -> None:
            """
            activate actions of the end of the round.
            updates the round's number
            """
 
            
            self.round+=1

        def is_over(self) -> bool:
            """
            checks if the game needs to be over now. returns True or False
            """
            in_bound=self.check_snake_head_in_bound()
            if not in_bound:
                return True
            hit_himself=self.__snake_hit_himself()
            if hit_himself:
                return True
            
            head_in_walls = self.check_snake_head_in_walls()
            if head_in_walls:
                return True
           
            if_one=self.check_if_one()
            if if_one:
              return True 
            
            if self.args.rounds >= 0:
                if self.round > self.args.rounds:
                    return True
            
            return False
        
        
        def add_objects(self)->None:
            """
            adds a wall and apples
            """
            self.__add_wall()
            self.__add_apples()

        def __in_bound(self, loc: tuple[int, int]) -> bool:
            """
            checks if a given location is in the board's borders
            return True or False
            """
            x, y = loc
            if not (0 <= x < self.args.width):
                return False
            if not (0 <= y < self.args.height):
                return False
            return True
        
        def __check_if_empty_lst(self,locs:list[tuple[int,int]]):
            """
            checks if a list of locations contains only empty locations
            returns True or False
            """
            locs_set=set(locs)
            in_snake=self.__check_in_snake(locs_set)
            
            if in_snake:
                return False
            in_walls=self.__check_in_walls(locs_set)
            
            if in_walls:
                return False
                        
            in_apples=self.__check_in_apples(locs_set)
            if in_apples:
                return False
            return True
        
        def __check_if_empty(self,loc:tuple[int,int]):
            """
            returns True if a given location is empty and False otherwise
            :param loc:
            :return:
            """
            return self.__check_if_empty_lst([loc])

        def __check_in_snake(self, locs_set):
            """
            returns True if a given loc is part of the snake
            """
            if self.__snake is None:
                return False
            snake_pos=self.__snake.get_snake_positions()
            is_common=utils.check_if_common_list(snake_pos,locs_set)
            return is_common
        
        def __check_in_walls(self, locs_set):
            """
            checks if a given loc set has a wall in it
            returns True or False
            """
            for wall in self.walls:
                wall_pos=wall.get_wall_locations()
                is_common=utils.check_if_common_list(wall_pos,locs_set)
                if is_common:
                   return True
            return False
            
            
        def __array_out_bound(self,ls:list[tuple[int,int]]):
            """
            checks if all locations in a list are out the borders
            returns True or False
            """
            for loc in ls:
                if self.__in_bound(loc):
                    return False
            return True

        def __move_snake(self):
            """
                Moves the snake in the game.

                This is a private method that moves the snake in the game based on the game logic.
                in case the snake exists.
                Returns:
                    None
            """
            if self.__snake is None:
                    return
            if self.grow > 0:
                self.__snake.add_length()
                self.grow-=1
            else:
                self.__snake.move_snake()
        
        def check_snake_head_in_bound(self):
            """
            checks if the snake's head is in the board
            returns True or False
            """
            if self.__snake is None:
                return True
            head=self.__snake.get_head()
            return self.__in_bound(head)
            
        def __draw_snake(self, gd: GameDisplay) -> None:
            """
            draw snake on the board
            """
            if self.__snake is None:
                return
            positions=self.__snake.get_snake_positions() 
            for loc in positions:
                if self.__in_bound(loc):
                    _x, _y = loc
                    gd.draw_cell(_x,_y, utils.BLACK)
            
                         
        def __snake_change_dir(self):
                if self.__key_clicked is  None:
                    return 
                if self.__snake is None:
                    return
                self.__snake.change_dir(self.__key_clicked)
        
        def __snake_hit_himself(self):
            """
            checks if the snake hit itself
            returns True or False
            """
            if self.__snake is None:
                return False
            hit_himself=self.__snake.check_if_hit_itself()
            if hit_himself:
                return True
            return False
        
        def check_if_one(self):
            """
            checks if only the head of the snake is left
            returns True of False
            """
            if self.__snake is None:
                return False
            l = len(self.__snake.get_snake_positions())
            if l <= 1:
                return True
            return False
            
        def __init_snake(self):
            """
            initiate the snake in the starting position
            """
            args=self.args
            if bool(args.debug):
                self.__snake=None
                return
            started_pos=args.width //2,args.height //2 
            self.__snake = Snake(started_pos)   
            

        def check_snake_head_in_walls(self):
            """
            check if the snake hit the walls
            returns true or false
            """
            if self.__snake is None:
                return False
            head = self.__snake.get_head()
            for wall in self.walls:
                if wall.is_wall(head):
                    return True
            return False
        
        def cut_snake_wall(self):
            """
            cuts the snake according to where the wall hit it
            """
            if self.__snake is None:
                return
            heads=self.get_heads()
            for head in heads:
                self.__snake.cut_snake(head)
                
        def check_snake_head_in_walls(self):
            """
            checks if the snake hit by the wall
            returns true or false
            """
            if self.__snake is None:
                return False
            head = self.__snake.get_head()
            for wall in self.walls:
                if wall.is_wall(head):
                    return True
            return False
        
        
        def __destroy_apple_in_walls(self):
            """
            get the apple away after it was hit by the wall
            """
            heads=self.get_heads()
            for head in heads:
                self.apples.remove_apple(head)
           
        
        def __eat_apple(self):
            """
            all actions after the snake eats an apple:
            adding to score and starting the growth
            """
            if self.__snake is None:
                    return
            head = self.__snake.get_head()
            is_eaten=self.apples.remove_apple(head)
            if not is_eaten:
                return 
            self.__add_score()
            self.grow+=3
            
        def __add_score(self):
            """
            adding and updating the score
            """
            length=len(self.__snake.get_snake_positions())
            raw_score=length**0.5
            self.score+=int(raw_score)
       
    
        