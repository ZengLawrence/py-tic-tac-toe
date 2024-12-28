""" Module implements game rules"""

import random
import copy


def init_state():
    """ Initialize state"""
    return [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def get_side(state, box):
    """Utility function to get side taken the box"""
    row, col = box
    return state[row-1][col-1]

def set_side(state, box, side):
    """Utility function to set side for the box"""
    row, col = box
    state[row-1][col-1] = side

class RuleViolation(Exception):
    """This is parent Exception class for rule violation."""

class InvalidMoveViolation(RuleViolation):
    """This exception raised when user makes an invalid move."""
class BoxTakenViolation(RuleViolation):
    """This exception raised when user put a piece to a box already taken,"""

def validate(move, state):
    """Check if a move is valid"""
    row, col = move
    if not ((0 < row < 4) and (0 < col < 4)):
        raise InvalidMoveViolation()
    if not get_side(state, move) == " ":
        raise BoxTakenViolation()

def next_side(side):
    """Return side for next move"""
    if side == 'x':
        return 'o'
    return 'x'

def all_three_same(row):
    """Return true if all three boxes in a row are the same side"""
    x, y, z = row
    return (x in 'xo') and (x == y) and (x == z)

def winner(state):
    """Return true if there is a winning row, column or diagonal"""
    return (
      all_three_same(state[0]) or
      all_three_same(state[1]) or
      all_three_same(state[2]) or
      all_three_same([state[0][0], state[1][0], state[2][0]]) or
      all_three_same([state[0][1], state[1][1], state[2][1]]) or
      all_three_same([state[0][2], state[1][2], state[2][2]]) or
      all_three_same([state[0][0], state[1][1], state[2][2]]) or
      all_three_same([state[0][2], state[1][1], state[2][0]])
      )

def tie(state):
    """Return true if game ends in a tie"""
    return all(val in 'xo' for row in state for val in row)

def computer_move(current_game):
    """Computer enters a randomly selected move."""
    move = random.choice(empty_boxes(current_game.state))
    current_game.make(move)

def empty_boxes(state):
    """Return all empty boxes on the board."""
    return [(i+1, j+1) for (i, row) in enumerate(state)
                        for (j, v) in enumerate(row)
                        if v == " "]

class Game:
    """Class representing game"""

    def __init__(self):
        self.state = init_state()
        self.side = 'x'
        self.result = None
        self.callback = None
        self.players = ['x', 'o']
        self.previous_move = None

    def start(self, players=None):
        """Starts game by calling callback function"""
        if players:
            self.players = players
        if 'x' in self.players:
            if self.callback:
                self.callback(self)
        else:
            computer_move(self)

    def register(self, callback):
        """Register callback function for state change event"""
        assert callable(callback)
        self.callback = callback

    def make(self, move):
        """
            Make a move -- a tuple of (row, col) in the game, throws subclass of RuleViolation 
            if not valid.
        """
        validate(move, self.state)
        previous_state = copy.deepcopy(self.state)
        previous_side = self.side
        set_side(self.state, move, self.side)
        if winner(self.state):
            self.result = self.side + " won"
        if tie(self.state):
            self.result = "tie"
        self.side = next_side(self.side)
        self.previous_move = (move, previous_side, previous_state)
        if self.callback:
            self.callback(self)
        if self.result is None and self.side not in self.players:
            computer_move(self)

if __name__ == "__main__":
    assert winner([['x', 'x', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']]), "first row is winner"
    assert winner([[' ', ' ', ' '], ['x', 'x', 'x'], [' ', ' ', ' ']]), "second row is winner"
    assert winner([[' ', ' ', ' '], [' ', ' ', ' '], ['x', 'x', 'x']]), "third row is winner"
    assert winner([['o', ' ', ' '], ['o', ' ', ' '], ['o', ' ', ' ']]), "first column is winner"
    assert winner([[' ', 'o', ' '], [' ', 'o', ' '], [' ', 'o', ' ']]), "second column is winner"
    assert winner([[' ', ' ', 'o'], [' ', ' ', 'o'], [' ', ' ', 'o']]), "third column is winner"
    assert winner([['x', ' ', ' '], [' ', 'x', ' '], [' ', ' ', 'x']]), "diagonal is winner"
    assert winner([[' ', ' ', 'o'], [' ', 'o', ' '], ['o', ' ', ' ']]), "diagonal is winner"
    assert tie([['o', 'x', 'x'], ['x', 'x', 'o'], ['o', 'o', 'x']]), "tie"

    running_game = [['o', 'x', 'x'], [' ', 'x', 'o'], ['o', 'o', 'x']]
    assert not (winner(running_game) or tie(running_game)), "game is still running"

    game = Game()
    assert empty_boxes(game.state) == [
        (1,1), (1,2), (1,3),
        (2,1), (2,2), (2,3),
        (3,1), (3,2), (3,3)]
