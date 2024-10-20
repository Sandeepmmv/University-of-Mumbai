import random

board = [" " for _ in range(9)]

def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def is_board_full(board):
    return " " not in board

def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def min_max(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = min_max(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = min_max(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_move = -1
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_eval = min_max(board, 0, False)
            board[i] = " "
            if move_eval > best_eval:
                best_eval = move_eval
                best_move = i
    board[best_move] = "O"

while True:
    display_board(board)
    user_input = input("Enter your move (0-8): ")
    user_input = int(user_input)
    
    if board[user_input] == " ":
        board[user_input] = "X"
        
        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            break
        
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        ai_move(board)
        
        if check_winner(board, "O"):
            display_board(board)
            print("AI wins!")
            break
