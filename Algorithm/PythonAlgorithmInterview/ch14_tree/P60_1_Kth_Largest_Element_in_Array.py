from typing import List
import heapq


class P60_1_Kth_Largest_Element_in_Array:
    def findKthLargest(self, nums:List[int], k:int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)