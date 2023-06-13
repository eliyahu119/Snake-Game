import sys
from importlib import import_module
from io import StringIO
import json
from ast import literal_eval

from argparse import Namespace


def snake_runner(modulename, fname, args=[], kwargs={}, options={}, tname=''):
    module = import_module(modulename)
    func = getattr(module, fname)
    exception = getattr(module, 'GameException')
    try:
        res = func(*args, **kwargs)
    except getattr(module, 'GameException') as e:
        print(e)
        return 'error', 'Game state was wrong'
    if res:
        return 'wrong', 'wrong'
    return None, None


defaults = {'modulename': 'game_display',
            'runner': snake_runner,
            'fname': 'rungame',
            'ans': [None],
            }
BASEDIR = '.'


def read_recorded_game(filename):
    with open(filename) as f:
        rec = json.load(f)
        # print(rec['grids'])
        return (rec['seed'],
                Namespace(**rec['args']),
                rec['inputs'],
                [(r[0], {literal_eval(k): v for k, v in r[1].items()})
                 for r in rec['grids']],
                )


cases = {filename: {'args': read_recorded_game(f'{BASEDIR}/{filename}.json')}
         for filename in [
             'empty',
             'debug1',
             'debug2',
             'nomoves',
             'turns',
             'odd',
             'many',
             'selfcrash1',
             'selfcrash2',
             'wallcrash',
             'cutting',
             'scorecut',
]}
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


if __name__ == '__main__':
    from game_display import GameDisplay, GameException
    c = 0
    for filename, args in cases.items():
        print("_"*20)
        print("_"*20)
        print("running", filename)
        print("_"*20)
        print(args["args"][1])
        print("_"*20)
        try:
            GameDisplay(*(args["args"])).start()
            print("*"*20)
            print("*"+" "*6+"PASSED"+" "*6+"*")
            print("*"*20)
            c += 1
        except GameException as e:
            if e.previous:
                print("previous board")
                print("score", e.previous[0], "round", e.round-1)
                print_board(generate_board(e.dim.height, e.dim.width, e.previous[1]))
            if e.expected:
                print("expected board")
                print("score", e.expected[0], "round", e.round)
                print_board(generate_board(e.dim.height, e.dim.width, e.expected[1]))
            print("your board:")
            print("score", e.actual[0], "round", e.round)
            print_board(generate_board(e.dim.height, e.dim.width, e.actual[1]))
            
            print("*"*20)
            print("*"+" "*6+"FAILED"+" "*6+"*")
            print("*"*20)
    print(f"pass {c}/{len(cases)}")
