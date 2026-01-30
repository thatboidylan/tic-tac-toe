def create_board():
  return[[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
  
def display_board(board):
  for row in board:
    print(row)
    
board = create_board()
display_board(board)
