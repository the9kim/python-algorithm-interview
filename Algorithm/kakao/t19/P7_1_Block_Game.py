from typing import List


class P7_1_Block_Game:
    '''
    1. Sliding two types of windows cross the 2-Dimensional Array
    2. Check if each window contains a block and determine if the block is removable
    3. Remove any removable block and slide the windows again from the beginning.
    '''

    def solution(self, board: List[List[int]]) -> int:
        def is_empty_above(r: int, c: int) -> bool:
            while r >= 0:
                if board[r][c] != 0:
                    return False
                r -= 1
            return True

        def can_block(r: int, c: int, w: int, h: int) -> bool:
            zero_num = 0
            last_val = -1

            for row in range(r, r + h):
                for col in range(c, c + w):
                    if board[row][col] == 0:
                        if zero_num >= 2 or not is_empty_above(row, col):
                            return False
                        zero_num += 1
                    else:
                        if last_val != -1 and last_val != board[row][col]:
                            return False
                        last_val = board[row][col]

            return True

        def remove(r: int, c: int, w: int, h: int) -> None:
            for row in range(r, r + h):
                for col in range(c, c + w):
                    board[row][col] = 0

        answer = 0

        condition = True
        while condition:
            cnt = 0

            for row in range(len(board)):
                for col in range(len(board[0])):
                    if row <= len(board) - 2 and col <= len(board[0]) - 3 and can_block(row, col, 3, 2):
                        cnt += 1
                        remove(row, col, 3, 2)

                    if row <= len(board) - 3 and col <= len(board) - 2 and can_block(row, col, 2, 3):
                        cnt += 1
                        remove(row, col, 2, 3)

            condition = cnt > 0
            answer += cnt

        return answer
