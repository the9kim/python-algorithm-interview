from typing import List

def solution(board: List[List[int]], skill: List[int]):
    '''
    1. Calculate the cumulative sum
    2. apply the cumulative sum to the input array
    '''

    row_size = len(board)
    col_size = len(board[0])

    # 1
    cumulative_sum = calc_cumulative_sum(skill, row_size, col_size)

    # 2
    return calc_undamaged_buildings(board, cumulative_sum)


def calc_cumulative_sum(skill: List[int], row_size: int, col_size: int) -> List[List[int]]:
    cumulative_sum = [[0 for _ in range(col_size + 1)] for _ in range(row_size + 1)]

    for t, r1, c1, r2, c2, degree in skill:
        degree = degree if t == 2 else -degree

        cumulative_sum[r1][c1] += degree
        cumulative_sum[r2 + 1][c1] -= degree
        cumulative_sum[r1][c2 + 1] -= degree
        cumulative_sum[r2 + 1][c2 + 1] += degree

    for c in range(col_size + 1):
        for r in range(1, row_size + 1):
            cumulative_sum[r][c] += cumulative_sum[r - 1][c]

    for r in range(row_size + 1):
        for c in range(1, col_size + 1):
            cumulative_sum[r][c] += cumulative_sum[r][c - 1]

    return cumulative_sum


def calc_undamaged_buildings(board: List[List[int]], cumulative_sum: List[List[int]]) -> int:
    undamaged_buildings = 0

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += cumulative_sum[r][c]
            if board[r][c] > 0:
                undamaged_buildings += 1

    return undamaged_buildings
