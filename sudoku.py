# Simple command-line Sudoku solver using backtracking

from typing import List, Optional, Tuple

Board = List[List[int]]

def print_board(board: Board) -> None:
    for r in range(9):
        line = " ".join(str(num) if num != 0 else '.' for num in board[r])
        print(line)


def find_empty(board: Board) -> Optional[Tuple[int, int]]:
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def is_valid(board: Board, num: int, pos: Tuple[int, int]) -> bool:
    r, c = pos
    # check row and column
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    # check 3x3 square
    start_r = (r // 3) * 3
    start_c = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == num:
                return False
    return True


def solve(board: Board) -> bool:
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for num in range(1, 10):
        if is_valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False


def main() -> None:
    print("Enter the puzzle row by row (use 0 for blanks):")
    board: Board = []
    for i in range(9):
        row_str = input(f"Row {i + 1}: ").strip()
        if len(row_str) != 9 or not row_str.isdigit():
            print("Invalid row. Must be exactly 9 digits (0-9).")
            return
        board.append([int(ch) for ch in row_str])

    if solve(board):
        print("Solved puzzle:")
        print_board(board)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
