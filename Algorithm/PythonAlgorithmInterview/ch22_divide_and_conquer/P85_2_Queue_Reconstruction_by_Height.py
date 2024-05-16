from typing import List
import heapq


class P85_1_Queue_Reconstruction_by_Height:
    def reconstructQueue(self, people:List[List[int]])-> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        answer = []
        while heap:
            person = heapq.heappop(heap)
            answer.insert(person[1], [-person[0], person[1]])

        return answer