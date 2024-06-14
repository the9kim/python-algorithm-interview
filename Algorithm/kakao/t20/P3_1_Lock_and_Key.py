from typing import List


class P3_1_Lock_and_Key:
    '''
    1. Utilize iteration to move the key on the padded lock.
    2. Rotate key
    3. Check if the key is valid
    '''
    def solution(self, key: List[List[int]], lock: List[List[int]]) -> bool:
        offset = len(key) - 1

        # 1.
        for row in range(0, len(lock) + offset):
            for col in range(0, len(lock) + offset):
                for _ in range(4):
                    padded_lock = self.getPaddedLock(lock, offset)
                    lock_with_key = self.insertKey(key, padded_lock, row, col)
                    # 3.
                    if self.isValidKey(lock_with_key, offset):
                        return True
                    # 2.
                    key = self.rotate(key)

        return False
    def getPaddedLock(self, lock, offset):
        padded_lock = [[0 for _ in range(len(lock[0]) + offset * 2)] for _ in range(len(lock) + offset * 2)]

        for r in range(len(lock)):
            for c in range(len(lock[0])):
                padded_lock[offset + r][offset + c] = lock[r][c]

        return padded_lock

    def insertKey(self, key, padded_lock, row, col):
        for r in range(len(key)):
            for c in range(len(key[0])):
                if padded_lock[row + r][col + c] == 1 and key[r][c] == 1:
                    padded_lock[row + r][col + c] = 0
                elif padded_lock[row + r][col + c] == 0 and key[r][c] == 1:
                    padded_lock[row + r][col + c] = key[r][c]

        return padded_lock

    def isValidKey(self, lock_with_key, offset):
        for r in range(offset, len(lock_with_key) - offset):
            for c in range(offset, len(lock_with_key[0]) - offset):
                if lock_with_key[r][c] == 0:
                    return False

        return True

    def rotate(self, key):
        rotated = [[0 for _ in range(len(key))] for _ in range(len(key))]
        for r in range(0, len(key)):
            for c in range(0, len(key[0])):
                rotated[r][c] = key[len(key[0]) - 1 - c][r]

        return rotated
