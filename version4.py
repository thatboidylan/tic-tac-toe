player_symbol = "X"
cpu_symbol = "O"

def create_board():
  return [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
  
def display_board(board):
  for row in board:
    print(row)
    
def get_player_choice(player_symbol):
  choice = int(input("Player " + player_symbol + " choose a number (1-9): "))
  return choice
  
def place_move(board, choice, player_symbol):
  for i in range(3):
    for j in range(3):
     if board[i][j] == choice:
       board[i][j] = player_symbol
  return board

board = create_board()

while True:
  display_board(board)
  choice = get_player_choice(player_symbol)
  board = place_move(board, choice, player_symbol)
