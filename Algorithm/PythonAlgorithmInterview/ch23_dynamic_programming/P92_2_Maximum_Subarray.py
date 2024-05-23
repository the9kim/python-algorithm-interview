from typing import List


class P92_2_Maximum_Subarray:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        current_sum = 0

        for i, n in enumerate(nums):
            current_sum = max(current_sum + n, n)
            max_sum = max(max_sum, current_sum)

        return max_sum