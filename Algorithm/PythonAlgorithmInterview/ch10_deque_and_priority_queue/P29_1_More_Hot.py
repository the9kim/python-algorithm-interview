import heapq


class P28_1_More_Hot:
    def solution(self, scoville: list[int], K: int) -> int:
        heap = []

        for val in scoville:
            heapq.heappush(heap, val)

        count = 0
        while len(heap) >= 2 and heap[0] < K:
            index = heapq.heappop(heap) + heapq.heappop(heap) * 2
            heapq.heappush(heap, index)
            count += 1

        return -1 if heap[0] < K else count