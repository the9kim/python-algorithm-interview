import bisect
from typing import List


class P72_1_Intersection_of_Two_Arrays:

    '''
    The solution to use two pointer strategy
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        intersection = set()

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.add(nums1[i])
                i += 1
                j += 1

        return list(intersection)








