#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    """Use backtracking to find all solutions"""
    if row == N:
        solutions.append(board[:])
    else:
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(N, row + 1, board, solutions)
                board[row] = -1

def print_solutions(N, solutions):
    """Print the solutions in the specified format"""
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)
    print_solutions(N, solutions)

if __name__ == "__main__":
    main()
