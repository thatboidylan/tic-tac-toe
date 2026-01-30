import random

player_symbol = "X"
cpu_symbol = "O"

def create_board():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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

def cpu_move(board):
    available = []
    for row in board:
        for cell in row:
            if isinstance(cell, int):
                available.append(cell)
    return random.choice(available)

def check_winner(board, player_symbol):
    for row in board:
        if all(cell == player_symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True

    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if isinstance(cell, int):
                return False
    return True

def play_game():
    board = create_board()
    player = "X"

    while True:
        display_board(board)

        if player == "X":
            choice = get_player_choice(player)
        else:
            print("Computer is choosing a move...")
            choice = cpu_move(board)

        place_move(board, choice, player)

        if check_winner(board, player):
            display_board(board)
            print("{player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

play_game()
