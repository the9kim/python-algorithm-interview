from typing import List


class P92_1_Maximum_Subarray:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] < 0:
                continue
            nums[i] += nums[i - 1]

        return max(nums)
