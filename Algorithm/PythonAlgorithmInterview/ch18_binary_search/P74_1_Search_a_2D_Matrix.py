from typing import List


class P74_1_Search_a_2D_Matrix:
    def searchMatrix(self, matrix:List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True

        return False