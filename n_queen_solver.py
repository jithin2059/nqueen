# n_queen_solver.py
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queen(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queen(board, col + 1):
                return True
            board[i][col] = 0
    return False

def get_solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queen(board, 0):
        return board
    else:
        return None
