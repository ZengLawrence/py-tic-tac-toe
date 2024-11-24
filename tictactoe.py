from game import Game, BoxTakenViolation

def print_board(state):
  b = ["--|---|--"] * 5
  sep = " | "
  b[0] = sep.join(state[0])
  b[2] = sep.join(state[1])
  b[4] = sep.join(state[2])
  for l in b:
    print(l)

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
      return (row, col)
    except ValueError:
      pass
  print(instruction)
  return enter_move(side)

print(instruction)
game = Game()
print_board(game.state)
while game.running():
  move = enter_move(game.side)
  try:
    game.make(move)
  except BoxTakenViolation:
    print("Box %s%s is taken" % move)
  except:
    print(instruction)
  else:
    print_board(game.state)
