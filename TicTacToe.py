# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there's a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Main function to run the game
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column numbers from 1 to 3): ")
        row, col = map(int, input().split())

        # Convert to 0-based index
        row -= 1
        col -= 1

        if board[row][col] != " ":
            print("This position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
