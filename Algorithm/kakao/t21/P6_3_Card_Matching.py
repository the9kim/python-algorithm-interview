from collections import defaultdict
from collections import deque


class Pointer:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist


cards = defaultdict(list)
n = 4
Board = None
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solution(board, r, c):
    global cards, n, Board

    Board = board

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                continue
            cards[board[row][col]].append(Pointer(row, col, 0))

    return permutate(Pointer(r, c, 0))


def permutate(curr: Pointer) -> int:
    if not cards:
        return 0

    min_cnt = float('inf')

    for num in range(1, 7):
        if num not in cards:
            continue

        card1 = cards[num][0]
        card2 = cards[num][1]

        cnt1 = cal_mani_count(curr, card1) + cal_mani_count(card1, card2) + 2
        cnt2 = cal_mani_count(curr, card2) + cal_mani_count(card2, card1) + 2

        cards.pop(num)

        min_cnt = min(min_cnt, cnt1 + permutate(card2))
        min_cnt = min(min_cnt, cnt2 + permutate(card1))

        cards[num].append(card1)
        cards[num].append(card2)

    return min_cnt


def cal_mani_count(src: Pointer, dst: Pointer) -> int:
    dq = deque()
    dq.append(src)
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[src.row][src.col] = True

    while dq:
        curr = dq.popleft()

        if curr.row == dst.row and curr.col == dst.col:
            return curr.dist

        for d in range(4):
            next_row = curr.row + directions[d][0]
            next_col = curr.col + directions[d][1]
            next_dist = curr.dist + 1

            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                continue

            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                dq.append(Pointer(next_row, next_col, next_dist))

            for i in range(2):
                if Board[next_row][next_col] in cards:
                    break
                if next_row + directions[d][0] < 0 or next_row + directions[d][0] >= n \
                        or next_col + directions[d][1] < 0 or next_col + directions[d][1] >= n:
                    break

                next_row += directions[d][0]
                next_col += directions[d][1]

            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                dq.append(Pointer(next_row, next_col, next_dist))