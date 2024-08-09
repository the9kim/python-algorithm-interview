from typing import List
import collections

class P7_1_Disappearing_Platform:
    '''
    1. Find the player's route and the opponent's route using DFS
    2. If It is expected to win based on the previous search, minimize the route; if expected to lose, maximize the route
    '''
    def solution(self, board: List[List[int]], aloc:List[int], bloc:List[int]) -> int:
        N = len(board)
        M = len(board[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1 ,0))
        def dfs(player_row: int, player_col : int, opponent_row :int, opponent_col :int) -> int:
            if board[player_row][player_col] == 0:
                return 0

            result = 0

            for row_step, col_step in directions:
                next_row = player_row + row_step
                next_col = player_col + col_step

                if next_row < 0 or next_row > N - 1 \
                    or next_col < 0 or next_col > M - 1 \
                    or board[next_row][next_col] == 0:
                    continue

                board[player_row][player_col] = 0
                move_count = dfs(opponent_row, opponent_col, next_row, next_col) + 1
                board[player_row][player_col] = 1

                if result % 2 == 0 and move_count % 2 == 1:
                    result = move_count
                elif result % 2 == 0 and move_count % 2 == 0:
                    result = max(result, move_count)
                elif result % 2 == 1 and move_count % 2 == 1:
                    result = min(result, move_count)

            return result


        return dfs(aloc[0], aloc[1], bloc[0], bloc[1])




