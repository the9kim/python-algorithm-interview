from typing import List


class P1_1_Coloring_Book:
    def solution(self, m: int, n: int, picture: List[List[int]]):

        area_cnt = 0
        max_area = float('-inf')

        def dfs(r: int, c: int, picture: List[List[int]], pos_val: int) -> int:
            if r < 0 or c < 0 or r >= len(picture) or c >= len(picture[0]) or picture[r][c] == 0 or picture[r][c] != pos_val:
                return 0

            area_cnt = 1
            picture[r][c] = 0

            area_cnt += dfs(r, c + 1, picture, pos_val)
            area_cnt += dfs(r + 1, c, picture, pos_val)
            area_cnt += dfs(r, c - 1, picture, pos_val)
            area_cnt += dfs(r - 1, c, picture, pos_val)

            return area_cnt

        for r in range(m):
            for c in range(n):
                if picture[r][c]:
                    area_cnt += 1
                    max_area = max(max_area, dfs(r, c, picture, picture[r][c]))

        return [area_cnt, max_area]

