from typing import List
import heapq


class P61_1_Double_Priority_Queue:
    def solution(self, operations:List[str]) -> List[int]:
        min_heap = list()
        max_heap = list()

        for operation in operations:
            o = operation.split(" ")
            if "I" == o[0]:
                e = int(o[1])
                heapq.heappush(min_heap, e)
                heapq.heappush(max_heap, -e)

            elif "D" == o[0]:
                if "1" == o[1]:
                    if len(max_heap) != 0:
                        e = heapq.heappop(max_heap)
                        min_heap.remove(-e)

                elif "-1" == o[1]:
                    if len(min_heap) != 0:
                        e = heapq.heappop(min_heap)
                        max_heap.remove(-e)

        if len(max_heap) == 0 and len(min_heap) == 0:
            return [0, 0]

        return [-max_heap[0], min_heap[0]]
