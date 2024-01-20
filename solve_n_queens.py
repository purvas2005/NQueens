# solve_n_queens.py

from solve_n_queens_util import solve_n_queens_util

def solve_n_queens(n):
    # Initialize the chessboard with all zeros
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    #if len(solutions)==0:
        #return "Enter Valid Input"
    return solutions
