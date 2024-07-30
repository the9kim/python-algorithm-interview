import itertools
from typing import List
from itertools import permutations


class P6_2_Exteral_Wall_Inspection:
    '''
    The solution using permutations

    1. Iterate through every weak point
    2. Calculate permutations of people sequence and iterate through each permutation during every weak point iteration
    3. Check if each permutation can complete the inspection and update the minimum number of people required
    '''

    def solution(self, n: int, weak: List[int], dist: List[int]):
        weak_size = len(weak)
        min_people = float('inf')
        weak += [w + n for w in weak]

        # 1.
        for start in range(weak_size):

            # 2.
            for d in itertools.permutations(dist, len(dist)):
                cnt = 1
                curr = start

                for i in range(1, weak_size):
                    next = start + i
                    diff = weak[next] - weak[curr]

                    if diff > d[cnt - 1]:
                        cnt += 1
                        curr = next

                        if cnt > len(dist):
                            break

                # 3.
                if cnt <= len(dist):
                    min_people = min(min_people, cnt)

        if min_people == float('inf'):
            return -1

        return min_people








