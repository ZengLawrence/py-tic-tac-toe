"""Module to start the console based game."""

import random
import sys
from game import Game, BoxTakenViolation, RuleViolation

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
    if len(move_input) == 2:
        try:
            row = int(move_input[0])
            col = int(move_input[1])
            return (row, col)
        except ValueError:
            pass
    print(INSTRUCTION)
    return enter_move(side)

def user_move(game):
    """User enters a move."""
    move = enter_move(game.side)
    try:
        game.make(move)
    except BoxTakenViolation:
        print(f"Box {move[0]}{move[1]} is taken")
    except RuleViolation:
        print(INSTRUCTION)
    else:
        print_board(game.state)

def computer_move(game):
    """Computer enters a randomly selected move."""
    move = random.choice(game.empty_boxes())
    print(f"Computer takes {move[0]}{move[1]} for {game.side}.")
    game.make(move)
    print_board(game.state)

def print_result(game):
    """Print game result."""
    print(game.result)

def enter_players():
    """Get number of players from console and return the number"""
    n = input("How many players (1 or 2): ")
    if n in ('1', '2'):
        return int(n)
    return enter_players()

def enter_side():
    """Get side for human player from console and return the side"""
    side = input("Choose side (x or o): ")
    if side in "xo":
        return side
    return enter_side()

class Console:
    """Class represent console based game. Used for user interactions."""
    def start(self):
        """Start console game"""
        two_player_game = user_move
        if enter_players() == 1:
            human_side = enter_side()
            def one_player_game(game):
                """Game for one player"""
                if game.side == human_side:
                    return user_move(game)
                return computer_move(game)
            per_move = one_player_game
        else:
            per_move = two_player_game
        print(INSTRUCTION)
        Game().start(per_move, done = print_result)
