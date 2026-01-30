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
