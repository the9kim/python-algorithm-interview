from typing import List

N = 0
Board = None
total_removals = 0


def solution(board: List[List[int]]) -> int:
    '''
    1. Sliding two types of windows and find the blocks
    2. If those block can be removable
    '''
    global N, Board, total_removals

    N = len(board)
    Board = board

    while True:
        removed_blocks = 0

        removed_blocks += check_blocks(2, 3)
        removed_blocks += check_blocks(3, 2)

        if not removed_blocks:
            break

        total_removals += removed_blocks

    return total_removals


def check_blocks(height: int, width: int) -> int:
    removed_blocks = 0

    for row in range(0, N - height + 1):
        for col in range(N - width + 1):
            if can_remove(row, col, height, width):
                remove_block(row, col, height, width)
                removed_blocks += 1

    return removed_blocks


def can_remove(row: int, col: int, height: int, width: int) -> bool:
    empty_count = 0
    block_value = -1

    for r in range(row, row + height):
        for c in range(col, col + width):
            if Board[r][c] == 0:
                if empty_count >= 2 or not is_above_empty(r, c):
                    return False
                empty_count += 1

            else:
                if block_value != -1 and block_value != Board[r][c]:
                    return False
                block_value = Board[r][c]

    return True


def is_above_empty(row: int, col: int) -> None:
    while row >= 0:
        if Board[row][col] != 0:
            return False
        row -= 1
    return True


def remove_block(row: int, col: int, height: int, width: int) -> None:
    for r in range(row, row + height):
        for c in range(col, col + width):
            Board[r][c] = 0
