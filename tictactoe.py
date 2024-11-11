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

token = input("Select x or o: ")
print("You select", token)

print_board(state)

while True:
  move = input("Enter a move:")
  row = int(move[0])
  col = int(move[1])
  state[row][col] = token
  print_board(state)