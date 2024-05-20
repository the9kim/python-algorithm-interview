from typing import List
import heapq


class P85_1_Queue_Reconstruction_by_Height:
    def reconstructQueue(self, people:List[List[int]])-> List[List[int]]:
        heap = [(-person[0], person[1], person) for person in people]
        heapq.heapify(heap)

        answer = []
        while heap:
            person = heapq.heappop(heap)[2]
            answer.insert(person[1], person)

        return answer