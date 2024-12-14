""" Module implements game rules"""

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

def no_ops(_game):
    """Place holder function that take one argument 'game'"""

class Game:
    """Class representing game"""

    def __init__(self):
        self.state = init_state()
        self.side = 'x'
        self.result = None
        self.per_move = no_ops
        self.done = no_ops

    def __running(self):
        """Return true if game is running. Game ends if there is a winner or a tie."""
        return self.result is None

    def start(self, per_move, done):
        """
            Starts game. Execute per_move function repeatedly while the game is running, 
            and done function when the game ends.

            Both per_move and done function takes game instance as input.
        """
        if per_move:
            self.per_move = per_move
        if done:
            self.done = done
        self.__per_move()

    def __per_move(self):
        if self.per_move:
            self.per_move(self)
            if self.__running():
                self.__per_move()
            else:
                self.done(self)

    def make(self, move):
        """
            Make a move -- a tuple of (row, col) in the game, throws subclass of RuleViolation 
            if not valid.
        """
        validate(move, self.state)
        set_side(self.state, move, self.side)
        if winner(self.state):
            self.result = self.side + " won"
        if tie(self.state):
            self.result = "tie"
        self.side = next_side(self.side)

    def empty_boxes(self):
        """Return all empty boxes on the board."""
        return [(i+1, j+1) for (i, row) in enumerate(self.state)
                           for (j, v) in enumerate(row)
                           if v == " "]

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
    assert Game.empty_boxes(game) == [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
