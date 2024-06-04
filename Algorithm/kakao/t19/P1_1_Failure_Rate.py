import heapq
from typing import List


class P1_1_Failure_Rate:
    def solution(self, N: int, stages: List[int]) -> int:
        # 1. Calculate Failure rates(number of players on the stage / rest users)
        rest = len(stages)
        heap = []
        for n in range(1, N + 1):
            if rest == 0:
                heapq.heappush(heap, (0, n))
                continue

            users = stages.count(n)
            rate = users / rest

            rest -= users

            # 2. Sort stages in descending order of failure rates using Heap
            heapq.heappush(heap, (-rate, n))


        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])

        return answer
