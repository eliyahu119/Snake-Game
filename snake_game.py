from typing import Optional
from game_display import GameDisplay
from snake import Snake
from wall import Wall
from apple import Apple
import game_utils
import utils


class SnakeGame:
        

        def __init__(self, args) -> None:
            self.args = args
            self.__key_clicked = None
            self.round = 0
            self.score = 0
            self.grow = 0
            self.apples_eaten=0            
            
            self.__init_snake()
            self.__init_walls()
            self.__init_apples()
        
       
        def __add_score(self):
            length=len(self.__snake.get_snake_positions())
            raw_score=length**0.5
            self.score+=int(raw_score)

        def __init_apples(self):
            self.apples=Apple()
            
        def __add_apples(self):
            if len(self.apples.get_apples_loc())>=self.args.apples:
                return False
            apple=game_utils.get_random_apple_data()
            if not self.__check_if_empty(apple):
                return False
            self.apples.add_apple(apple)
            return True
       
        def __check_in_apples(self,loc:set[tuple[int,int]]):
            apples=self.apples.get_apples_loc()
            return utils.check_if_common_list(loc,apples)
            
        def __draw_apples(self, gd: GameDisplay) -> None:
            positions=self.apples.get_apples_loc() 
            for loc in positions:
                if self.__in_bound(loc):
                    _x, _y = loc
                    gd.draw_cell(_x,_y, utils.GREEN)
                    
        def __init_snake(self):
            args=self.args
            started_pos=args.width //2,args.height //2 
            self.__snake = Snake(started_pos)
            # for i in range(10):
            #     self.__snake.add_length()
            # self.__snake.add_length()
            
            # self.apple = Apple

        #region walls
        def __init_walls(self):
            self.walls:list[Wall]=[]
            # self.__add_wall()

        def __add_wall(self):
            wall_len=len(self.walls)
            if wall_len > self.args.walls:
                return False
            wall=self.__get_valid_wall()
            if wall is None:
                return False
            self.walls.append(wall)
            return True
            
        def __get_valid_wall(self):
            # while True:
                x,y,d=game_utils.get_random_wall_data()
                wall=Wall((x,y),d)
                locs=wall.get_wall_locations()
                is_empty=self.__check_if_empty_lst(locs)
                if is_empty:
                    return wall
                else:
                    return None
                # self.__snake.get_snake_positions()
                
        def __draw_walls(self,gd):
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
            if self.round == 0 or self.round % 2 == 1:
                return 
            for wall in self.walls:
                wall.move_wall()
        
        def __remove_out_borders_walls(self)->None:
            new_arr=[]
            for wall in self.walls:
                pos=wall.get_wall_locations()
                in_bound=self._array_in_bound(pos)
                if in_bound:
                    new_arr.append(wall)
            self.walls=new_arr
        
        def get_heads(self):
            return list(map(lambda x:x.get_head(),self.walls))
        #endregion

        #region Public_functions
        def read_key(self, key_clicked: Optional[str]) -> None:
            self.__key_clicked = key_clicked

        def update_objects(self) -> None:
            
            self.change_dir_objects()
            self.move_objects()
            
        def change_dir_objects(self):
            self.__snake_change_dir()
            # self.__walls_change_dir()

        def move_objects(self):
            self.__move_walls()
            self.__move_snake()

        def draw_board(self, gd: GameDisplay) -> None:
            self. __draw_snake(gd)
            self.__draw_walls(gd)
            self.__draw_apples(gd)

        def end_round(self) -> None:
            self.cut_snake_wall()
            self.__remove_out_borders_walls()
            self.__destroy_apple_in_walls()
            self.__eat_apple()
            
            self.round+=1

        def is_over(self) -> bool:
            in_bound=self.check_snake_head_in_bound()
            if not in_bound:
                return True
            hit_himself=self.__snake.check_if_hit_itself()
            if hit_himself:
                return True
            
            head_in_walls = self.check_snake_head_in_walls()
            if head_in_walls:
                return True
           
            l = len(self.__snake.get_snake_positions())
            if l <= 1:
                return True
        
            if self.round == self.args.rounds:
                return True
            
            return False
        
        
        def add_objects(self)->None:
            self.__add_wall()
            self.__add_apples()
        #endregion

        #region help
        def __in_bound(self, loc: tuple[int, int]) -> bool:
            x, y = loc
            if not (0 <= x < self.args.width):
                return False
            if not (0 <= y < self.args.height):
                return False
            return True
        
        def __check_if_empty_lst(self,locs:list[tuple[int,int]]):
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
            return self.__check_if_empty_lst([loc])


        def __check_in_snake(self, locs_set):
            snake_pos=self.__snake.get_snake_positions()
            is_common=utils.check_if_common_list(snake_pos,locs_set)
            return is_common
        
        def __check_in_walls(self, locs_set):
            for wall in self.walls:
                wall_pos=wall.get_wall_locations()
                is_common=utils.check_if_common_list(wall_pos,locs_set)
                if is_common:
                   return True
            return False
            
        def _array_in_bound(self,ls:list[tuple[int,int]]):
            for loc in ls:
                if not self.__in_bound(loc):
                    return False
                return True
        #endregion
                
        #region snake
        def __move_snake(self):
            if self.grow > 0:
                self.__snake.add_length()
                self.grow-=1
            else:
                self.__snake.move_snake()
        
        def check_snake_head_in_bound(self):
            head=self.__snake.get_head()
            return self.__in_bound(head)
            
        def __draw_snake(self, gd: GameDisplay) -> None:
            positions=self.__snake.get_snake_positions() 
            for loc in positions:
                if self.__in_bound(loc):
                    _x, _y = loc
                    gd.draw_cell(_x,_y, utils.BLACK)
            
                         
        def __snake_change_dir(self):
                if self.__key_clicked is not None:
                    self.__snake.change_dir(self.__key_clicked)
        #endregion

        #region collision
        def check_snake_head_in_walls(self):
            head = self.__snake.get_head()
            for wall in self.walls:
                if wall.is_wall(head):
                    return True
            return False
        
        def cut_snake_wall(self): 
            #will not cut if the head is colliding with the head
            #or if the head is not present in the snake.
            heads=self.get_heads()
            for head in heads:
                self.__snake.cut_snake(head)
                
        def check_snake_head_in_walls(self):
            head = self.__snake.get_head()
            for wall in self.walls:
                if wall.is_wall(head):
                    return True
            return False
        
        
        def __destroy_apple_in_walls(self):
            heads=self.get_heads()
            for head in heads:
                self.apples.remove_apple(head)
           
        
        def __eat_apple(self):
            head = self.__snake.get_head()
            is_eaten=self.apples.remove_apple(head)
            if not is_eaten:
                return 
            self.__add_score()
            self.grow+=3
            # self.score+=3
            # self.groth+=3
        #endregion
