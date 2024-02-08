import heapq
import math

class P28_1_K_Closest_Points_to_Origin:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (distance, point))


        answer = []
        for i in range(k):
            p = heapq.heappop(heap)
            answer.append(p[1])

        return answer




