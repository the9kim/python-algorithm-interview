import collections
from typing import List


class Point:
    def __init__(self, row: int, col: int, cnt: int):
        self.row = row
        self.col = col
        self.cnt = cnt


class P6_1_Card_Matching:
    '''
    Time-exceeded

    1. Calculate permutations of the order in which the cards are flipped
    2. Calculate the distance between pairs of cards from the current distance using BFS
    '''

    def solution(self, board: List[List[int]], r: int, c: int) -> int:
        size = len(board)

        D = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(src: Point, dst: Point) -> int:
            visited = [[False for _ in range(size)] for _ in range(size)]

            q = collections.deque()
            q.append(src)
            visited[src.row][src.col] = True

            while q:
                curr = q.popleft()
                if curr.row == dst.row and curr.col == dst.col:
                    return curr.cnt

                for dir in range(4):
                    next_row = curr.row + D[dir][0]
                    next_col = curr.col + D[dir][1]

                    if next_row < 0 or next_row > size - 1 or next_col < 0 or next_col > size - 1:
                        continue

                    if not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        q.append(Point(next_row, next_col, curr.cnt + 1))

                    for _ in range(2):
                        if board[next_row][next_col] != 0:
                            break

                        if next_row + D[dir][0] < 0 or next_row + D[dir][0] > size - 1 or next_col + D[dir][
                            1] < 0 or next_col + D[dir][1] > size - 1:
                            break

                        next_row += D[dir][0]
                        next_col += D[dir][1]

                    if not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        q.append(Point(next_row, next_col, curr.cnt + 1))

        def permute(curr: Point) -> int:
            min_cnt = float('inf')

            for sym in range(1, 7):
                cards = []
                for row in range(size):
                    for col in range(size):
                        if board[row][col] == sym:
                            cards.append(Point(row, col, 0))

                if not cards:
                    continue

                d1 = bfs(curr, cards[0]) + bfs(cards[0], cards[1]) + 2
                d2 = bfs(curr, cards[1]) + bfs(cards[1], cards[0]) + 2

                for card in cards:
                    board[card.row][card.col] = 0

                min_cnt = min(min_cnt, d1 + permute(cards[1]))
                min_cnt = min(min_cnt, d2 + permute(cards[0]))

                for card in cards:
                    board[card.row][card.col] = sym

            if min_cnt == float('inf'):
                return 0

            return min_cnt

        return permute(Point(r, c, 0))
