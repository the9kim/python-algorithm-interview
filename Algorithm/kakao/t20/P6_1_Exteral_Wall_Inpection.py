from typing import List


class P6_1_Exteral_Wall_Inspection:
    '''
    Time-Exceeded

    1. Iterate through the input array, weak points
    2. Check if people can check every weak point at each iteration
    3. Determine the minimum number of people required to inspect the points.
    '''

    def solution(self, n: int, weak: List[int], dist: List[int]):
        weak_size = len(weak)

        global min_cnt
        min_cnt = float('inf')

        def inspect(cnt: int, pos: int, visited: int) -> None:
            global min_cnt

            if cnt > len(dist):
                return
            if cnt >= min_cnt:
                return

            for i in range(weak_size):
                next_pos = (pos + i) % weak_size
                diff = weak[next_pos] - weak[pos]
                if next_pos < pos:
                    diff += n
                if diff > dist[len(dist) - cnt]:
                    break
                visited |= 1 << next_pos

            if visited == ((1 << weak_size) - 1):
                min_cnt = cnt
                return

            for i in range(weak_size):
                if (visited & (1 << i)) != 0:
                    continue
                inspect(cnt + 1, i, visited)

        for i in range(weak_size):
            inspect(1, i, 0)

        if min_cnt == float('inf'):
            return -1

        return min_cnt
