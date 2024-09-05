from sys import setrecursionlimit
from typing import Set

DIRECTIONS = ((1, 0), (0, -1), (0, 1), (-1, 0))
VECTOR = ("d", "l", "r", "u")
optimal_path = "impossible"


def solution(n: int, m: int, x: int, y: int, r: int, c: int, k: int):
    setrecursionlimit(5000)

    dfs((x - 1, y - 1), (r - 1, c - 1), k, 0, n, m, "")

    return optimal_path


def dfs(src: Set[int], dst: Set[int], movement_count: int, curr_count: int, row_size: int, col_size: int, path: str):
    global optimal_path

    if curr_count > movement_count:
        return

    if not can_escape(src, dst, movement_count - curr_count):
        return

    if curr_count == movement_count and src[0] == dst[0] and src[1] == dst[1]:
        optimal_path = path
        return

    for i, d in enumerate(DIRECTIONS):
        next_row = src[0] + d[0]
        next_col = src[1] + d[1]

        if not can_move(next_row, next_col, row_size, col_size):
            continue

        path += VECTOR[i]

        dfs((next_row, next_col), dst, movement_count, curr_count + 1, row_size, col_size, path)

        if optimal_path != "impossible":
            return

        path = path[:-1]


def can_move(next_row: int, next_col: int, row_size: int, col_size: int) -> bool:
    return 0 <= next_row < row_size and 0 <= next_col < col_size


def can_escape(src: Set[int], dst: Set[int], movement_left: int):
    distance = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
    return distance <= movement_left and (movement_left - distance) % 2 == 0
