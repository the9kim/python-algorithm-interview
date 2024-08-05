import collections
from typing import List, Tuple, Dict

class P6_2_Card_Matching:
    def __init__(self):
        self.board = []
        self.cards = collections.defaultdict(list)
        self.all_removed = 1
        self.min_cnt = float('inf')
        self.D = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def solution(self, board: List[List[int]], r: int, c: int) -> int:
        self.board = board

        for i in range(4):
            for j in range(4):
                num = board[i][j]
                if num != 0:
                    self.all_removed |= 1 << num
                    self.cards[num].append((i, j, 0))

        self.permute(0, 1, (r, c, 0))
        return self.min_cnt

    def permute(self, cnt: int, removed: int, src: Tuple[int, int, int]):
        if cnt >= self.min_cnt:
            return

        if removed == self.all_removed:
            self.min_cnt = min(self.min_cnt, cnt)
            return

        for num, card in self.cards.items():
            if removed & (1 << num):
                continue

            n1 = self.bfs(removed, src, card[0]) + self.bfs(removed, card[0], card[1]) + 2
            n2 = self.bfs(removed, src, card[1]) + self.bfs(removed, card[1], card[0]) + 2

            self.permute(cnt + n1, removed | (1 << num), card[1])
            self.permute(cnt + n2, removed | (1 << num), card[0])

    def bfs(self, removed: int, src: Tuple[int, int, int], dst: Tuple[int, int, int]) -> int:
        visited = [[False for _ in range(4)] for _ in range(4)]
        q = collections.deque()
        q.append(src)
        visited[src[0]][src[1]] = True

        while q:
            curr = q.popleft()
            if curr[0] == dst[0] and curr[1] == dst[1]:  # Correct condition
                return curr[2]

            for dir in range(4):
                next_row, next_col = curr[0] + self.D[dir][0], curr[1] + self.D[dir][1]

                if 0 <= next_row < 4 and 0 <= next_col < 4 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, curr[2] + 1))

                # Jump to the next card
                while 0 <= next_row + self.D[dir][0] < 4 and 0 <= next_col + self.D[dir][1] < 4 and \
                        (removed & (1 << self.board[next_row][next_col])) != 0:
                    next_row += self.D[dir][0]
                    next_col += self.D[dir][1]

                if 0 <= next_row < 4 and 0 <= next_col < 4 and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    q.append((next_row, next_col, curr[2] + 1))

        return float('inf')  # If not reachable

