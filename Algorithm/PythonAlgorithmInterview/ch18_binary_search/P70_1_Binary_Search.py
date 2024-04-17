from typing import List


class P70_1_Binary_Search:

    # Recursive solution
    def search(self, nums:List[int], target: int) -> int:
        def binarySearch(left: int, right: int) -> int:
            mid = left + (right - left) // 2
            while left <= right:
                if target < nums[mid]:
                    return binarySearch(left, mid - 1)
                elif target > nums[mid]:
                    return binarySearch(mid + 1, right)
                else:
                    return mid

            return -1

        return binarySearch(0, len(nums) - 1)


