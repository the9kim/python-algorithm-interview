from typing import List


def solution(key: List[List[int]], lock: List[List[int]]) -> bool:
    offset = len(key) - 1

    for row in range(0, offset + len(lock)):
        for col in range(0, offset + len(lock[0])):

            for _ in range(0, 4):
                expanded = expand_key(lock, offset)
                paste_key_to_lock(expanded, key, row, col)

                if can_unlock(expanded, offset):
                    return True

                key = rotate(key)

    return False


def expand_key(lock: List[List[int]], offset: int) -> List[List[int]]:
    expanded = [[0 for _ in range(len(lock[0]) + 2 * offset)] for _ in range(len(lock) + 2 * offset)]

    for r in range(len(lock)):
        for c in range(len(lock[0])):
            expanded[r + offset][c + offset] = lock[r][c]

    return expanded


def paste_key_to_lock(expanded: List[List[int]], key: List[List[int]], row_offset: int, col_offset: int) -> None:
    for r in range(len(key)):
        for c in range(len(key[0])):
            if expanded[row_offset + r][col_offset + c] == 1 and key[r][c] == 1:
                expanded[row_offset + r][col_offset + c] = 0
            elif expanded[row_offset + r][col_offset + c] == 0 and key[r][c] == 1:
                expanded[row_offset + r][col_offset + c] = 1


def can_unlock(expanded: List[List[int]], offset: int) -> bool:
    for r in range(offset, len(expanded) - offset):
        for c in range(offset, len(expanded) - offset):
            if expanded[r][c] == 0:
                return False

    return True


def rotate(key: List[List[int]]) -> List[List[int]]:
    rotated = [[0 for _ in range(len(key[0]))] for _ in range(len(key))]

    for r in range(len(key)):
        for c in range(len(key[0])):
            rotated[len(key) - 1 - c][r] = key[r][c]

    return rotated
