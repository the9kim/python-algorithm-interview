import bisect
from typing import List


class P73_1_Two_Sum:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            expected = target - n
            idx = bisect.bisect_left(numbers, expected, i+1, len(numbers))
            if idx < len(numbers) and numbers[idx] == expected:
                return [i + 1, idx + 1]

        return None
