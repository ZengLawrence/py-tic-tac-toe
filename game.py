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

def all_three_same(row):
  x, y, z = row
  return (x in 'xo') and (x == y) and (x == z)

def winning(state):
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
  return all(val in 'xo' for row in state for val in row)

class Game:
  def __init__(self):
    self.state = init_state()
    self.side = 'x'
    self.result = None

  def running(self):
    return self.result is None

  def make(self, move):
    # make a move -- tuple of (row, col) in the game, through exception if not valid
    validate(move, self.state)
    set(self.state, move, self.side)
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
