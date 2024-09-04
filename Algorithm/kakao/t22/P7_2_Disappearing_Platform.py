from typing import List

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solution(board: List[List[int]], aloc: List[int], bloc: List[int]) -> int:
    '''
    1. find a path by taking turns
    2. update the optimal paths among existing paths
    '''

    return dfs(aloc[0], aloc[1], bloc[0], bloc[1], board)


def dfs(player_row: int, player_col: int, opponent_row: int, opponent_col: int, board: List[List[int]]) -> int:
    if board[player_row][player_col] == 0:
        return 0

    optimal_movements = 0

    for row_movement, col_movement in DIRECTIONS:
        next_player_row = player_row + row_movement
        next_player_col = player_col + col_movement

        if not can_move(next_player_row, next_player_col, board):
            continue

        board[player_row][player_col] = 0

        movements = dfs(opponent_row, opponent_col, next_player_row, next_player_col, board) + 1

        board[player_row][player_col] = 1

        if optimal_movements % 2 == 0 and movements % 2 == 1:
            optimal_movements = movements
        elif optimal_movements % 2 == 1 and movements % 2 == 1:
            optimal_movements = min(optimal_movements, movements)
        elif optimal_movements % 2 == 0 and movements % 2 == 0:
            optimal_movements = max(optimal_movements, movements)

    return optimal_movements


def can_move(next_row: int, next_col: int, board: List[List[int]]) -> bool:
    return 0 <= next_row < len(board) and 0 <= next_col < len(board[0]) and board[next_row][next_col] != 0
