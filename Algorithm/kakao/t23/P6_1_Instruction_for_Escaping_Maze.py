import sys

class P6_1_Instruction_for_Escaping_Maze:
    def solution(self, n: int, m: int, x :int, y: int, r: int, c: int, k: int) -> str:
        sys.setrecursionlimit(5000)

        directions = ((1, 0), (0, -1), (0, 1), (-1, 0))
        commands = ("d", "l", "r", "u")
        route = []
        result = ""

        distance = self.get_distance(x, y, r, c)
        if distance > k or (k - distance) % 2 != 0:
            return "impossible"

        def dfs(row, col, step):
            nonlocal result

            if result != "":
                return
            if k - step < self.get_distance(row, col, r, c):
                return

            if step == k:
                result = ''.join(route)

            for i in range(4):
                next_row = row + directions[i][0]
                next_col = col + directions[i][1]
                next_step = step + 1

                if next_row < 1 or next_row > n or next_col < 1 or next_col > m:
                    continue

                route.append(commands[i])
                dfs(next_row, next_col, next_step)
                route.pop()

        dfs(x, y, 0)

        return result

    def get_distance(self, r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)