from typing import List


class P75_1_Immigration:
    def solution(self, n: int, times: List[int]) -> int:
        left = 0
        right = max(times) * n

        mid = right

        while left <= right:
            calcN = 0
            for time in times:
                calcN += mid // time

            if n <= calcN:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1

            mid = left + (right - left) // 2

        return answer
