def print_board(b):
    print(f"{b[0]}|{b[1]}|{b[2]}\n-+-+-\n{b[3]}|{b[4]}|{b[5]}\n-+-+-\n{b[6]}|{b[7]}|{b[8]}\n")

def winner(b, p):
    W = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i] == b[j] == b[k] == p for i,j,k in W)

def minimax(b, is_ai):
    if winner(b,'O'): return 1
    if winner(b,'X'): return -1
    if ' ' not in b: return 0
    scores = []
    for i in range(9):
        if b[i]==' ':
            b[i] = 'O' if is_ai else 'X'
            scores.append(minimax(b, not is_ai))
            b[i] = ' '
    return max(scores) if is_ai else min(scores)

def best_move(b):
    best_score = -99; move = None
    for i in range(9):
        if b[i]==' ':
            b[i]='O'
            score=minimax(b, False)
            b[i]=' '
            if score>best_score:
                best_score, move = score, i
    return move

# --------------------- MAIN GAME ---------------------
board = [' '] * 9
print("Welcome to Tic-Tac-Toe!")
print("You = X, AI = O")
print_board(board)

while True:
    pos = input("Your move (1-9): ")
    if not pos.isdigit() or not (1 <= int(pos) <= 9) or board[int(pos)-1] != ' ':
        print("Invalid move! Try again.")
        continue
    board[int(pos)-1] = 'X'
    print_board(board)
    if winner(board,'X'): print("You win!"); break
    if ' ' not in board: print("Draw!"); break

    ai = best_move(board)
    board[ai] = 'O'
    print(f"AI placed O at {ai+1}")
    print_board(board)
    if winner(board,'O'): print("AI wins!"); break
    if ' ' not in board: print("Draw!"); break
