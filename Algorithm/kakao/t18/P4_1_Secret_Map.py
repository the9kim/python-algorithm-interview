from typing import List


class P_1_Secret_Map:
    def solution(self, m: int, n: int, board: List[str]) -> int:

        matrix = [list(x) for x in board]

        matched = True

        while matched:
            matched = []

            # 1. Find blocks
            for row in range(m -1):
                for col in range(n - 1):
                    if matrix[row][col] == \
                            matrix[row][col + 1] == \
                            matrix[row + 1][col] == \
                            matrix[row + 1][col + 1] != '0':
                        matched.append([row, col])

            # 2. Remove blocks
            for row, col in matched:
                matrix[row][col] = matrix[row][col + 1] = matrix[row + 1][col] = matrix[row + 1][col + 1] = '0'

            # 3. Move blocks
            for _ in range(m):
                for i in range(m - 1):
                    for j in range(n):
                        if matrix[i + 1][j] == '0':
                            matrix[i][j], matrix[i + 1][j] = '0', matrix[i][j]


        # 4. Calculate the number of removed blocks
        return sum(x.count('0') for x in matrix)

