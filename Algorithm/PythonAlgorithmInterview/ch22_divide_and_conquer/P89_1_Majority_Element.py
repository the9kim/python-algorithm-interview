from typing import List


class P89_1_Majority_Element:
    def majorityElement(self, nums: List[int]) -> int:
        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = left + (right - left) // 2

            n1 = divide_and_conquer(left, mid)
            n2 = divide_and_conquer(mid + 1, right)

            count = 0

            for i in range(left, right + 1):
                if n1 == nums[i]:
                    count += 1

            if count > (right - left + 1) // 2:
                return n1
            else:
                return n2

        return divide_and_conquer(0, len(nums) - 1)