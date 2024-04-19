import bisect
from typing import List


class P72_1_Intersection_of_Two_Arrays:

    '''
    The solution to use binary search module
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Sort the second array which is the target for binary search
        nums2 = sorted(nums2)

        # 2. Utilize iteration on the first array and check if another array contains each value from the first array
        intersection = set()
        for num in nums1:
            index = bisect.bisect_left(nums2, num)
            if index < len(nums2) and nums2[index] == num:
                intersection.add(num)

        return list(intersection)
