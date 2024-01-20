# solve_n_queens_util.py

from is_safe import is_safe

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # All queens are placed successfully, add the solution
        solution = [[board[i][j] for j in range(n)] for i in range(n)]
        solutions.append(solution)
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            
            # Recur for the next row
            solve_n_queens_util(board, row + 1, n, solutions)

            # Backtrack: remove the queen from the current cell
            board[row][col] = 0
