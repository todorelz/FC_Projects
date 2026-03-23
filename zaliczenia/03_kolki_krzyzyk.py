import math

PLAYER = "O"
COMPUTER = "X"
EMPTY = "-"

board = [EMPTY] * 9
def print_board():
    for i in range(0, 9, 3):
        print("".join(board[i:i+3]))
    print()


def check_winner(symbol):
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in winning_combinations)


def is_draw():
    return EMPTY not in board
def minimax(is_maximizing):
    if check_winner(COMPUTER):
        return 1
    if check_winner(PLAYER):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = COMPUTER
                score = minimax(False)
                board[i] = EMPTY
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                score = minimax(True)
                board[i] = EMPTY
                best = min(best, score)
        return best


def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = COMPUTER
            score = minimax(False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = COMPUTER


def player_move():
    while True:
        try:
            move = int(input())
            if move < 1 or move > 9 or board[move-1] != EMPTY:
                print("Błąd")
            else:
                board[move-1] = PLAYER
                break
        except ValueError:
            print("Błąd")


# --- GRA ---
while True:
    # Ruch komputera
    computer_move()
    print_board()

    if check_winner(COMPUTER):
        print("Przegrana")
        break

    if is_draw():
        print("Remis")
        break

    # Ruch gracza
    player_move()
    print_board()

    if check_winner(PLAYER):
        print("Wygrana")  # teoretycznie nigdy się nie zdarzy 😉
        break

    if is_draw():
        print("Remis")
        break
