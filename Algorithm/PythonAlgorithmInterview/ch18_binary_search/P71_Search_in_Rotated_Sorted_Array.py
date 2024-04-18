from typing import List


class P71_Search_in_Rotated_Sorted_Array:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find the pivot
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 2. Find the target position using the pivot
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            pivot_mid = (mid + pivot) % len(nums)

            if target < nums[pivot_mid]:
                right = mid - 1
            elif target > nums[pivot_mid]:
                left = mid + 1
            else:
                return pivot_mid

        return -1
