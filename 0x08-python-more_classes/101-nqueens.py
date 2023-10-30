#!/usr/bin/python3
"""N queens puzzle is the challenge"""


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a specific position \
            (row, col) on the chessboard.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row where we want to place the queen.
        col (int): The column where we want to place the queen.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen at the given \
                position, False otherwise.
    """
    # Check the column on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a chessboard of size N.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of solutions, where each solution is \
                a list of (row, column) positions for queens.
    """
    if n < 4:
        return []

    def solve(board, col):
        if col == n:
            solutions.append([[i, row] for i, row in enumerate(board)])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(board, col + 1)
                board[i][col] = 0

    solutions = []
    solve([[0] * n for _ in range(n)], 0)
    return solutions


def print_solutions(solutions):
    """
    Print the N-Queens solutions to the console.

    Args:
        solutions (list): A list of solutions, where each solution \
                is a list of (row, column) positions for queens.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
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

    solutions = solve_nqueens(N)
    print_solutions(solutions)
