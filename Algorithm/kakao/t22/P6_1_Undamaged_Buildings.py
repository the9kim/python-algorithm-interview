from typing import List

class P6_1_Undamaged_Building:
    '''
    1. Calculate the cumulative sum for each element in the matrix
    2. Apply the cumulative sums across the entire input board
    '''
    def solution(self, board: List[List[int]], skill: List[List[int]]) -> int:
        N = len(board)
        M = len(board[0])

        # 1.
        cumulative_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        for type, r1, c1, r2, c2, degree in skill:
            degree = -degree if type == 1 else degree

            cumulative_sum[r1][c1] += degree
            cumulative_sum[r2 + 1][c1] -= degree
            cumulative_sum[r1][c2 + 1] -= degree
            cumulative_sum[r2 + 1][c2 + 1] += degree

        for col in range(M + 1):
            for row in range(1, N + 1):
                cumulative_sum[row][col] += cumulative_sum[row - 1][col]

        for row in range(N + 1):
            for col in range(1, M + 1):
                cumulative_sum[row][col] += cumulative_sum[row][col - 1]


        # 2.
        building_count = 0

        for row in range(N):
            for col in range(M):
                board[row][col] += cumulative_sum[row][col]
                if board[row][col] > 0:
                    building_count += 1

        return building_count
