from typing import List
import heapq

class P60_3_Kth_Largest_Element_in_Array:
    def findKthLargest(self, nums:List[int], k:int) -> int:

        return heapq.nlargest(k, nums)[-1]

