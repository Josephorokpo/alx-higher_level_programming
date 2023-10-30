#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen in the given position.

    Args:
        board (list): The current chessboard state.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, otherwise False.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solve the N-queens puzzle for a given board size.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: A list of solutions, each represented as a list \
                of queen positions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col == n:
            solution = []
            for row in board:
                solution.append([i, row.index(1)])
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve(col + 1)
                board[i][col] = 0

    solve(0)
    return solutions


def main():
    """Main function to handle command-line input and display solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]

    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main":
    main()
