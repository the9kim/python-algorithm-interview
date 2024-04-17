import bisect
from typing import List


class P70_1_Binary_Search:

    # Binary Search Module
    def search(self, nums:List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index

        return -1


