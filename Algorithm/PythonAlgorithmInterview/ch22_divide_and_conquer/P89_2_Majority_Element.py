from typing import List


class P89_1_Majority_Element:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2

        n1 = self.majorityElement(nums[:half])
        n2 = self.majorityElement(nums[half:])

        return [n2, n1][nums.count(n1) > half]
