# ----- Check winner -----
def winner(b, p):
    W = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i] == b[j] == b[k] == p for i,j,k in W)

# ----- Minimax Function -----
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

# ----- Show all possible moves and scores -----
def show_scores(board):
    print("\nMove | Score")
    print("-----+-------")
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            print(f"  {i+1}  |   {score}")

# ----- Demo Board -----
board = ['X',' ',' ',' ','O',' ',' ',' ',' ']
show_scores(board)
