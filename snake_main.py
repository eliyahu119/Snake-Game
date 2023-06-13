import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

# 3


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame(args)
    gd.show_score(0)
    game.add_objects()
    # DRAW BOARD
    game.draw_board(gd)
    game.end_round()
    gd.end_round()
    while not game.is_over():

        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()

        game.check_collisions()
        # ADD OBjects
        game.add_objects()

        # DRAW BOARD
        game.draw_board(gd)
        gd.show_score(game.score)

        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
