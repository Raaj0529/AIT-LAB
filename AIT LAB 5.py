import math

def print_board(b):
    for i in range(3):
        print(b[3*i], b[3*i+1], b[3*i+2])
    print()

def winner(b):
    win_states = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b1,c in win_states:
        if board[a] == board[b1] == board[c] and board[a] != "_":
            return board[a]
    return None

def moves(b):
    return [i for i in range(9) if b[i] == "_"]

def minimax(b, depth, is_max):
    w = winner(b)
    if w == "O": return 1
    if w == "X": return -1
    if "_" not in b: return 0

    if is_max:
        best = -math.inf
        for m in moves(b):
            b[m] = "O"
            val = minimax(b, depth+1, False)
            b[m] = "_"
            best = max(best, val)
        return best
    else:
        best = math.inf
        for m in moves(b):
            b[m] = "X"
            val = minimax(b, depth+1, True)
            b[m] = "_"
            best = min(best, val)
        return best

def best_move(b):
    best_val = -math.inf
    best_index = None
    for m in moves(b):
        b[m] = "O"
        val = minimax(b, 0, False)
        b[m] = "_"
        if val > best_val:
            best_val = val
            best_index = m
    return best_index

board = ["_"] * 9

while True:
    print_board(board)

    if winner(board) or "_" not in board:
        break

    x = int(input("Enter position (0-8): "))
    if board[x] != "_":
        print("Invalid")
        continue
    board[x] = "X"

    if winner(board) or "_" not in board:
        break

    o = best_move(board)
    board[o] = "O"

print_board(board)

w = winner(board)
if w:
    print(w, "wins")
else:
    print("Draw")

