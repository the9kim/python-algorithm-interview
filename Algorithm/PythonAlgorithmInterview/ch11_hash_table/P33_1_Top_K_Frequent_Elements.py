import heapq
from typing import List
import collections

class P33_1_Top_K_Frequent_Elements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)

        most_common = freqs.most_common(k)
        answer = []
        for i in range(k):
            answer.append(most_common[i][0])

        return answer


    # Heap
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)

        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(freqs_heap)[1])

        return answer