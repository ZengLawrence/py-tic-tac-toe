state = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

def print_board(state):
  b = ["--|---|--"] * 5
  sep = " | "
  b[0] = sep.join(state[0])
  b[2] = sep.join(state[1])
  b[4] = sep.join(state[2])
  for l in b:
    print(l)

next_moves = { 'x': 'o', 'o': 'x'}
instruction = "Enter 2 digits for the move, for example, 11 for row 1 and column 1. 'q' to quit."

def enter_move(side):
  # get user entered move and return (row, col)
  move = input("Enter a move for " + side + ": ")
  if move == 'q':
    exit()
  if (len(move) == 2):
    try:
      row = int(move[0])
      col = int(move[1])
      return ((row, col), side, next_moves[side])
    except ValueError:
      pass
  print(instruction)
  return enter_move(side)

def validate(move):
  row, col = move
  if not ((row > 0 and row < 4) and (col > 0 and col < 4)):
    return (False, instruction)
  return (True, None)


def select_token():
  token = input("Select x or o: ")
  if (token not in 'xo'):
    print("Must select x or o.")
    return select_token()
  else:
    return token

token = select_token()
print("You select", token)
print_board(state)
side = 'x'
while True:
  move, curr_side, next_side = enter_move(side)
  is_valid, err_msg = validate(move)
  if is_valid:
    row, col = move
    state[row-1][col-1] = curr_side
    print_board(state)
    side = next_side
  else:
    print(err_msg)