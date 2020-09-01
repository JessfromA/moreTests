#*** Python Battleship V2***

from random import randint

board = []

for x in range(0, 6):
  board.append(["O"] * 6)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
ship_row1 = random_row(board)
ship_col1 = random_col(board)
nonsunkships = 2
print ship_row
print ship_col
print ship_row1
print ship_col1

for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row1 and guess_col == ship_col1) :
    print "Congratulations! You sank a battleship!"
    board[guess_row][guess_col] = "Z"
    nonsunkships -= 1
    if nonsunkships == 0:
      print "Congratulations! You sank all of the battleships, You Win !!"
      break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print("Game Over")
    print_board(board)

'''
to do:
lets transform the ship row/ship col variables into something we can iterate so we can have more than 2 ships by modifying very little code.
'''
