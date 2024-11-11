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

def enter_move():
  # get user entered move and return (row, col)
  move = input("Enter a move:")
  return (int(move[0]), int(move[1]))

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
while True:
  row, col = enter_move()
  state[row][col] = token
  print_board(state)