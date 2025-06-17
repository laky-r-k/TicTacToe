
def best_move(board,tac):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == 1:
            board[i] = 'o'
            score = minimax(board, 0, False,tac)
            board[i] = 1
            if score > best_score:
                best_score = score
                move = i
    return move

def minimax(board, depth, is_maximizing,tac):
    score = check(board,tac)
    if score is not None:
        return score

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == 1:
                board[i] = "o"
                val = minimax(board, depth + 1, False,tac)
                board[i] = 1
                best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == 1:
                board[i] = "x"
                val = minimax(board, depth + 1, True,tac)
                board[i] = 1
                best = min(best, val)
        return best

def check(board,tac):
    player = tac.check_win(board)
    if tac.check_tie(board) and player == -1:
        return 0
    elif player == 1:
        return -1  # human wins
    elif player == 2:
        return 1   # AI wins
    return None  # game not over
