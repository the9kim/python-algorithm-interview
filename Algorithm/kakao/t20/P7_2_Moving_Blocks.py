from typing import List
from collections import deque

class Point:
    def __init__(self, direction: int, row: int, col: int, dist: int):
        self.direction = direction
        self.row = row
        self.col = col
        self.dist = dist

Up = 0
RIGHT = 1
DOWN = 2
LEFT = 3

Board = None
N = 0
q = deque()
visited = None

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
rotations = (
    ((1, 1), (1, -1), (-1 , -1), (-1, 1)),
    ((1, -1), (-1, -1), (-1, 1), (1, 1))
)

corners = (
    ((-1, 1), (1, 1), (1, -1), (-1, -1)),
    ((-1, -1), (-1, 1), (1, 1), (1, -1))
)

def solution(board: List[List[int]]) -> int:
    global Board, N, visited, q

    Board = board
    N = len(board)
    visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(4)]

    visited[RIGHT][0][0] = True
    visited[LEFT][0][1] = True

    q.append([
        Point(RIGHT, 0, 0, 0),
        Point(LEFT, 0, 1, 0)
    ])

    while q:
        curr_points = q.popleft()

        for d in range(4):
            next_points = []
            for p in curr_points:
                next_points.append(
                    Point(
                        p.direction,
                        p.row + directions[d][0],
                        p.col + directions[d][1],
                        p.dist + 1
                    )
                )

            if canMove(next_points):
                if is_destination(next_points):
                    return next_points[0].dist
                update_route(next_points)
                q.append(next_points)

        for cw in range(2):
            for piv_idx in range(2):
                rotated_idx = (piv_idx + 1) % 2

                next_points = [None, None]
                pivot = curr_points[piv_idx]
                rotated = curr_points[rotated_idx]

                next_points[piv_idx] = Point(
                    (pivot.direction + (1 if cw == 0 else 3)) % 4,
                    pivot.row,
                    pivot.col,
                    pivot.dist + 1
                )

                next_points[rotated_idx] = Point(
                    (rotated.direction + (1 if cw == 0 else 3)) % 4,
                    rotated.row + rotations[cw][pivot.direction][0],
                    rotated.col + rotations[cw][pivot.direction][1],
                    rotated.dist + 1
                )

                if canMove(next_points) and can_rotate(pivot, cw):
                    if is_destination(next_points):
                        return next_points[0].dist
                    update_route(next_points)
                    q.append(next_points)

    return -1


def canMove(points: List[Point]) -> bool:
    for p in points:
        if p.row < 0 or p.col < 0 or p.row >= N or p.col >= N:
            return False
        if Board[p.row][p.col] == 1:
            return False

        if visited[p.direction][p.row][p.col]:
            return False

    return True

def is_destination(points: List[Point]) -> bool:
    for p in points:
        if p.row == N - 1 and p.col == N - 1:
            return True

    return False

def update_route(points: List[Point]) -> None:
    for p in points:
        visited[p.direction][p.row][p.col] = True

def can_rotate(point: Point, cw: int) -> bool:
    corner_row = point.row + corners[cw][point.direction][0]
    corner_col = point.col + corners[cw][point.direction][1]

    if Board[corner_row][corner_col] == 1:
        return False

    return True
