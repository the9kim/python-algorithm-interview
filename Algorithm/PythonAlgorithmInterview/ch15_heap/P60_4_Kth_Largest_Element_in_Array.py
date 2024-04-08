from typing import List
import heapq


class P60_4_Kth_Largest_Element_in_Array:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
