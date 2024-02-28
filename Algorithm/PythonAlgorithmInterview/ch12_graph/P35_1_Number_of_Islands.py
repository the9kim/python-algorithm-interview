from typing import List


class P36_1_Number_of_Islands:
    def numsIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid: List[List[str]], row: int, column:int):
            if column >= len(grid[0]) or column < 0 or row >= len(grid) or row < 0 or grid[row][column] == '0':
                return

            grid[row][column] = '0'

            dfs(grid, row, column + 1)
            dfs(grid, row + 1, column)
            dfs(grid, row - 1, column)
            dfs(grid, row, column - 1)


        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1

        return count



if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    p36 = P36_1_Number_of_Islands()
    count = p36.numsIslands(grid)
    print(count)

