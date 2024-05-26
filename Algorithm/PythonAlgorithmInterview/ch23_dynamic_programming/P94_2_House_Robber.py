from typing import List


class P94_1_House_Robber:

    # The book solution using recursive Brute force
    def rob(self, nums: List[int]) -> int:
        def _rob(n: int) -> int:
            if n < 0:
                return 0

            return max(_rob(n - 1), _rob(n - 2) + nums[n])

        return _rob(len(nums) - 1)
