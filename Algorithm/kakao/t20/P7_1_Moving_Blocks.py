import collections
from typing import List


class Point:
    def __init__(self, row: int, col: int, dir: int, time: int):
        self.row = row
        self.col = col
        self.dir = dir
        self.time = time


class P7_1_Moving_Blocks:
    '''
    BFS
    1. Move straight forward and rotate the robot
    2. Update the visitation record and determine the shortest time to reach the destination
    '''

    def solution(self, board: List[List[int]]) -> int:
        size = len(board)

        UP = 0
        RIGHT = 1
        DONW = 2
        LEFT = 3

        D = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        D_rot = [[[1, 1], [1, -1], [-1, -1], [-1, 1]],
                 [[1, -1], [-1, -1], [-1, 1], [1, 1]]]
        D_cor = [[[-1, 1], [1, 1], [1, -1], [-1, -1]],
                 [[-1, -1], [-1, 1], [1, 1], [1, -1]]]

        visited = [[[False for _ in range(size)] for _ in range(size)] for _ in range(4)]

        q = collections.deque()
        q.append([Point(0, 0, RIGHT, 0), Point(0, 1, LEFT, 0)])
        visited[RIGHT][0][0] = True
        visited[LEFT][0][1] = True

        while q:
            curr = q.popleft()

            for dir in range(4):
                next = []
                for p in curr:
                    next.append(
                        Point(
                            p.row + D[dir][0],
                            p.col + D[dir][1],
                            p.dir,
                            p.time + 1
                        ))
                if not self.can_move(next, board, visited):
                    continue

                for p in next:
                    if p.row == size - 1 and p.col == size - 1:
                        return p.time
                    visited[p.dir][p.row][p.col] = True
                q.append(next)

            for cw in range(2):
                for piv in range(2):
                    next = [None] * 2

                    pivot = piv
                    rotated = (piv + 1) % 2

                    next[pivot] = Point(
                        curr[pivot].row,
                        curr[pivot].col,
                        (curr[pivot].dir + (1 if cw == 0 else 3)) % 4,
                        curr[pivot].time + 1
                    )

                    next[rotated] = Point(
                        curr[rotated].row + D_rot[cw][curr[pivot].dir][0],
                        curr[rotated].col + D_rot[cw][curr[pivot].dir][1],
                        (curr[rotated].dir + (1 if cw == 0 else 3)) % 4,
                        curr[rotated].time + 1
                    )

                    if not self.can_move(next, board, visited):
                        continue

                    row_cor = curr[pivot].row + D_cor[cw][curr[pivot].dir][0]
                    col_cor = curr[pivot].col + D_cor[cw][curr[pivot].dir][1]
                    if board[row_cor][col_cor] == 1:
                        continue

                    for p in next:
                        if p.row == size - 1 and p.col == size - 1:
                            return p.time
                        visited[p.dir][p.row][p.col] = True

                    q.append(next)

        return 0

    def can_move(self, curr: List[Point], board: List[List[int]], visited: List[List[List[bool]]]):
        for p in curr:
            if p.row < 0 or p.row > len(board) - 1 or p.col < 0 or p.col > len(board) - 1:
                return False
            if board[p.row][p.col] == 1:
                return False
            if visited[p.dir][p.row][p.col]:
                return False

        return True
