"""Main module to start the console based game."""

import sys
from game import Game, BoxTakenViolation

def print_board(state):
    """Print game to the console."""
    b = ["--|---|--"] * 5
    sep = " | "
    b[0] = sep.join(state[0])
    b[2] = sep.join(state[1])
    b[4] = sep.join(state[2])
    for l in b:
        print(l)

INSTRUCTION = "Enter 2 digits for the move, for example, 11 for row 1 and column 1. 'q' to quit."

def enter_move(side):
    """get user entered move and return (row, col)"""
    move_input = input("Enter a move for " + side + ": ")
    if move_input == 'q':
        sys.exit()
    if (len(move_input) == 2):
        try:
            row = int(move_input[0])
            col = int(move_input[1])
            return (row, col)
        except ValueError:
            pass
    print(INSTRUCTION)
    return enter_move(side)

print(INSTRUCTION)
game = Game()
print_board(game.state)
while game.running():
    move = enter_move(game.side)
    try:
        game.make(move)
    except BoxTakenViolation:
        print("Box %s%s is taken" % move)
    except:
        print(INSTRUCTION)
    else:
        print_board(game.state)
print(game.result)
