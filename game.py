""" Module implements game rules"""

def init_state():
    """ Initialize state"""
    return [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def get_side(state, move):
    """Utility function to get side taken the box"""
    row, col = move
    return state[row-1][col-1]

def set_side(state, move, side):
    """Utility function to set side for the box"""
    row, col = move
    state[row-1][col-1] = side

class RuleViolation(Exception):
    """This is parent Exception class for rule violation."""

class InvalidMoveViolation(RuleViolation):
    """This exception raised when user makes an invalid move."""
class BoxTakenViolation(RuleViolation):
    """This exception raised when user put a piece to a box already taken,"""

def validate(move, state):
    """Check if move is valid"""
    row, col = move
    if not ((0 < row < 4) and (0 < col < 4)):
        raise InvalidMoveViolation()
    if not get_side(state, move) == " ":
        raise BoxTakenViolation()

def next_move(side):
    """Return side for next move"""
    if side == 'x':
        return 'o'
    return 'x'

def all_three_same(row):
    """Return true if all three in a row is the same side"""
    x, y, z = row
    return (x in 'xo') and (x == y) and (x == z)

def winning(state):
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

def stalemate(state):
    """Return true if game ends in stalemate"""
    return all(val in 'xo' for row in state for val in row)

class Game:
    """Class representing game"""

    def __init__(self):
        self.state = init_state()
        self.side = 'x'
        self.result = None

    def running(self):
        """Return true if game is running. Game ends if there is a winner or a stalemate."""
        return self.result is None

    def start(self, per_move, done):
        """
            Starts game. Execute per_move function repeatedly while the game is running, and done function when the game ends.

            Both per_move and done function takes game instance as input.
        """
        while self.running():
            per_move(self)
        done(self)

    def make(self, move):
        """Make a move -- tuple of (row, col) in the game, through exception if not valid"""
        validate(move, self.state)
        set_side(self.state, move, self.side)
        if winning(self.state):
            self.result = self.side + " won"
        if stalemate(self.state):
            self.result = "stalemate"
        self.side = next_move(self.side)

if __name__ == "__main__":
    assert winning([['x', 'x', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']]), "first row is winner"
    assert winning([[' ', ' ', ' '], ['x', 'x', 'x'], [' ', ' ', ' ']]), "second row is winner"
    assert winning([[' ', ' ', ' '], [' ', ' ', ' '], ['x', 'x', 'x']]), "third row is winner"
    assert winning([['o', ' ', ' '], ['o', ' ', ' '], ['o', ' ', ' ']]), "first column is winner"
    assert winning([[' ', 'o', ' '], [' ', 'o', ' '], [' ', 'o', ' ']]), "second column is winner"
    assert winning([[' ', ' ', 'o'], [' ', ' ', 'o'], [' ', ' ', 'o']]), "third column is winner"
    assert winning([['x', ' ', ' '], [' ', 'x', ' '], [' ', ' ', 'x']]), "diagonal is winner"
    assert winning([[' ', ' ', 'o'], [' ', 'o', ' '], ['o', ' ', ' ']]), "diagonal is winner"
    assert stalemate([['o', 'x', 'x'], ['x', 'x', 'o'], ['o', 'o', 'x']]), "stalemate"

    running_game = [['o', 'x', 'x'], [' ', 'x', 'o'], ['o', 'o', 'x']]
    assert not (winning(running_game) or stalemate(running_game)), "game is still running"
