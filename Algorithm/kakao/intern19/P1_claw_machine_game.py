from typing import List
from collections import defaultdict


class P1_claw_machine_game:
    def solution(self, board: List[List[int]], moves: List[int]) -> int:

        stack_board = self.create_stack_board(board)
        removed_dolls = self.pick_dolls(stack_board, moves)
        return removed_dolls

    def create_stack_board(self, board: List[List[int]]) -> defaultdict:
        stack_board = defaultdict(list)

        for c in range(len(board[0])):
            for r in range(len(board) - 1, -1, -1):
                if board[r][c]:
                    stack_board[c + 1].append(board[r][c])

        return stack_board

    def pick_dolls(self, stack_board: defaultdict, moves: List[int]):
        bucket = []
        removed_count = 0

        for move in moves:

            if stack_board[move]:
                picked = stack_board[move].pop()
                if bucket and picked == bucket[-1]:
                    removed_count += 2
                    bucket.pop()
                else:
                    bucket.append(picked)

        return removed_count
