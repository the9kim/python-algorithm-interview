from typing import List
import collections
from functools import cmp_to_key

class P3_1_Candidate_Key:
    '''
    1. Find subsets that meet uniqueness
    2. Sort the subsets in ascending order by the number of 1-bits
    3. Remove subsets that do not meet minimality
    '''
    def solution(self, relation: List[List[str]]) -> int:
        # 1.
        row_size = len(relation)
        col_size = len(relation[0])

        candidates = collections.deque([])

        for i in range(1, 1 << col_size):
            if self.is_unique(relation, row_size, col_size, i):
                candidates.append(i)

        # 2.
        candidates = sorted(candidates, key=cmp_to_key(self.compare))

        # 3.
        answer = 0

        while candidates:
            crnt = candidates.pop(0)
            answer += 1

            candidates = [next for next in candidates if (crnt & next) != crnt]

        return answer


    def is_unique(self, relation: List[List[str]], row_size: int, col_size: int, subset: int) -> bool:
        for r1 in range(0, row_size - 1):
            for r2 in range(r1 + 1, row_size):
                is_unique = False

                for d in range(0, col_size):
                    if (subset & (1 << d)) == 0:
                        continue
                    if relation[r1][d] != relation[r2][d]:
                        is_unique = True
                        break
                if not is_unique:
                    return False

        return True


    def compare(self, o1: int, o2: int) -> int:
        b1 = bin(o1).count("1")
        b2 = bin(o2).count("1")

        return b1 - b2




