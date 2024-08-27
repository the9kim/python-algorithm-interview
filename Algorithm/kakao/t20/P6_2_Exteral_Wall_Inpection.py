from itertools import permutations
from typing import List


class P6_2_Exteral_Wall_Inspection:
    '''
    The solution using permutations

    1. Iterate through every weak point
    2. Calculate permutations of people sequence and iterate through each permutation during every weak point iteration
    3. Check if each permutation can complete the inspection and update the minimum number of people required
    '''

    def solution(self, n: int, weak: List[int], dist: List[int]):
        weak_size = len(weak)
        weak += [n + w for w in weak]
        min_num = float('inf')

        for start in range(weak_size):
            for friends in permutations(dist):
                count = 1
                position = weak[start] + friends[count - 1]

                for step in range(start, start + weak_size):
                    if position < weak[step]:
                        count += 1
                        if count > len(dist):
                            break
                        position = weak[step] + friends[count - 1]

                min_num = min(min_num, count)

        if min_num > len(dist):
            return -1

        return min_num
