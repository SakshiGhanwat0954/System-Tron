def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
   
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2, space-separated): ").split())

        if board[row][col] != " ":
            print("Cell is already taken. Try again.")
            continue

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = 1 - turn  

tic_tac_toe()
