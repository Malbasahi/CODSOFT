import tkinter as tk
from tkinter import messagebox

# Constants for the Tic-Tac-Toe grid
GRID_SIZE = 3
GRID_WIDTH = 500
GRID_HEIGHT = 500
CELL_SIZE = GRID_WIDTH // GRID_SIZE

# Initialize the Tic-Tac-Toe board
board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initialize Tkinter
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize player and AI symbols
player_symbol = ''
ai_symbol = ''

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # Check for a tie
    if all(board[i][j] != ' ' for i in range(GRID_SIZE) for j in range(GRID_SIZE)):
        return True

    return False

# Function to evaluate the board for the AI (Minimax)
def evaluate(board):
    # Check rows, columns, and diagonals for wins
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            return 1
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return -1
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 1
        if board[0][i] == board[1][i] == board[2][i] == 'O':
            return -1
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        return -1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        return 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        return -1
    
    return 0  # Return 0 for a tie or undecided game

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if is_game_over(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = player_symbol
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] == ' ':
                    board[i][j] = ai_symbol
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to make the AI move
def ai_move():
    best_eval = float('-inf')
    best_move = None

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == ' ':
                board[i][j] = ai_symbol
                eval = minimax(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = ai_symbol
        update_board()
        if is_game_over(board):
            if evaluate(board) == 1:
                messagebox.showinfo("Game Over", f"{ai_symbol} wins!")
            else:
                messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()

# Function to handle player's move
def player_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = player_symbol
        update_board()
        if is_game_over(board):
            messagebox.showinfo("Game Over", f"{player_symbol} wins!")
            reset_board()
        else:
            ai_move()

# Function to update the GUI
def update_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell = board[i][j]
            buttons[i][j].config(text=cell, state='disabled' if cell != ' ' else 'normal')

# Function to reset the game
def reset_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            board[i][j] = ' '
            buttons[i][j].config(text=' ', state='normal')

# Function to let the player choose X or O
def choose_symbol(symbol):
    global player_symbol, ai_symbol
    player_symbol = symbol
    ai_symbol = 'X' if player_symbol == 'O' else 'O'
    ai_move()  # Let AI make the first move

# Create buttons for the player to choose X or O
x_button = tk.Button(root, text='Choose X', width=10, height=2, command=lambda: choose_symbol('X'))
o_button = tk.Button(root, text='Choose O', width=10, height=2, command=lambda: choose_symbol('O'))
x_button.grid(row=GRID_SIZE, column=0)
o_button.grid(row=GRID_SIZE, column=1)

# Create the buttons for the game grid
buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        buttons[i][j] = tk.Button(root, text=' ', width=10, height=2,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the Tkinter main loop
root.mainloop()
