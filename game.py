def init_state():
  return [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

def get(state, move):
  row, col = move
  return state[row-1][col-1]

def set(state, move, side):
  row, col = move
  state[row-1][col-1] = side

class RuleViolation(Exception): pass
class InvalidMoveViolation(RuleViolation): pass
class BoxTakenViolation(RuleViolation): pass

def validate(move, state):
  row, col = move
  if not ((row > 0 and row < 4) and (col > 0 and col < 4)):
    raise InvalidMoveViolation()
  if not (get(state, move) == " "):
    raise BoxTakenViolation()

def next_move(side):
  if side == 'x':
    return 'o'
  else:
    return 'x'
class Game:
  def __init__(self):
    self.state = init_state()
    self.side = 'x'

  def running(self):
    return True;

  def make(self, move):
    # make a move -- tuple of (row, col) in the game, through exception if not valid
    validate(move, self.state)
    set(self.state, move, self.side)
    self.side = next_move(self.side)
