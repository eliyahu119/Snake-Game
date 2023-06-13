#!/usr/bin/env python3

import sys
import getopt
import threading
import time
import tkinter as tki
from typing import Any, Optional, List, Tuple, Dict

import argparse
from argparse import Namespace

import game_utils

CELL_SIZE = 15
ROUND_TIME = 100

WIDTH = 40
HEIGHT = 30
NUM_OF_APPLES = 3
NUM_OF_WALLS = 2


class GameException(Exception):
    def __init__(self, round, actual, expected, previous, dim: game_utils.Size):
        super().__init__(f"""Round {round}: Error:
Game state differs from expected.
Last round:       {previous}
Current expected: {expected}
Current actual:   {actual}""")
        self.actual = actual
        self.expected = expected
        self.previous = previous
        self.dim = dim
        self.round = round


CHAR = "__"
COLORS = {"blue": f'\x1b[0;34;44m{CHAR}\x1b[0m', "green": f'\x1b[0;32;42m{CHAR}\x1b[0m',
          "black": f'\x1b[0;30;40m{CHAR}\x1b[0m', "white": f'\x1b[0;37;47m{CHAR}\x1b[0m'}


def generate_board(num_of_rows, num_of_cols, colors):
    board = [[COLORS['white']
              for _ in range(num_of_cols)] for _ in range(num_of_rows)]
    for (j, i), color in colors.items():
        board[i][j] = COLORS[color]
    return board


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()




class GameDisplay:
    def __init__(self, seed, args: Namespace, inputs, exp) -> None:
        game_utils.set_random_seed(seed)
        game_utils.set_size(args.width, args.height)
        self.args = args
        self.exp = exp
        self.round = 0
        self.score = None
        self.canvas = {}
        self.inputs = inputs[::-1]

    def start(self) -> None:
        import snake_main
        snake_main.main_loop(self, self.args)

    def get_key_clicked(self) -> Optional[str]:
        if self.inputs:
            return self.inputs.pop()
        return None

    def draw_cell(self, x: int, y: int, color: str) -> None:
        self.canvas[x, y] = color

    def end_round(self) -> None:
        gamestate = (self.score, self.canvas)
        # print("score:", self.score)
        # print_board(generate_board(game_utils.size.height, game_utils.size.width, self.canvas))
        # input()

        if not self.exp:
            print(gamestate)
            self.round += 1
            self.canvas = {}
            return

        if self.round >= len(self.exp):
            raise GameException(self.round, gamestate, None, self.exp[-1], game_utils.size)
        if gamestate != self.exp[self.round]:
            raise GameException(self.round, gamestate, self.exp[self.round],
                                self.exp[self.round - 1] if self.round > 0 else None, game_utils.size)  # wrong output
        self.round += 1
        self.canvas = {}

    def show_score(self, val: Any) -> None:
        self.score = val


def rungame(*args):
    gd = GameDisplay(*args)
    gd.start()
    if gd.round < len(gd.exp):
        raise GameException(f"""Round {gd.round}: Error:
Game finished prematurely.
Last round: {gd.exp[gd.round-1]}
Next state: {gd.exp[gd.round]}""")  # game should not be over


def parse_args(argv: List[str]) -> Namespace:
    parser = argparse.ArgumentParser(
        prog='game_display.py',
        description='Runs snake game',
    )
    parser.add_argument('-x', '--width', type=int, default=WIDTH,
                        help='args.width: Game board width')
    parser.add_argument('-y', '--height', type=int, default=HEIGHT,
                        help='args.height: Game board height')
    parser.add_argument('-s', '--seed', default=None,
                        help='Seed for random number generator (not passed to game loop)')
    parser.add_argument('-a', '--apples', type=int, default=NUM_OF_APPLES,
                        help='args.apples: Number of apples')
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='args.debug: Debug mode with no snake')
    parser.add_argument('-w', '--walls', type=int, default=NUM_OF_WALLS,
                        help='args.walls: Number of walls')
    parser.add_argument('-r', '--rounds', type=int, default=-1,
                        help='args.rounds: Number of rounds')
    parser.add_argument('-t', '--delay', type=int, default=ROUND_TIME,
                        help='Delay between rounds in milliseconds (not passed to game loop)')
    parser.add_argument('-v', '--verbose',
                        action='count', default=0,
                        help='Print helpful debugging information (not passed to game loop, can be used multiple times)')
    return parser.parse_args(argv)


inputs = [None, 'Down', 'Right', 'Left', 'Down', 'Left', None]



def setup_game(args: Namespace) -> GameDisplay:
    seed = args.__dict__.pop('seed')
    args.__dict__.pop('verbose')
    args.__dict__.pop('delay')
    gd = GameDisplay(seed, args, inputs, None).start()


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    setup_game(args)
