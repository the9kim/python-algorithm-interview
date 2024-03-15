import heapq
from typing import List
import collections


class P45_1_Cheapest_Flight_Within_K_Stops:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k:int) -> int:

        graph = collections.defaultdict(list)

        for start, end, price in flights:
            graph[start].append([end, price])


        pq = [[0, src, 0]]

        visited = collections.defaultdict(list)

        while pq:
            price, node_id, level = heapq.heappop(pq)

            if node_id == dst:
                return price

            if level > k:
                continue

            visited[node_id] = level

            for next in graph[node_id]:
                new_id = next[0]
                new_price = price + next[1]
                new_level = level + 1

                if (new_id not in visited) or (new_level < visited[new_id]):
                    heapq.heappush(pq, [new_price, new_id, new_level])

        return -1


if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1

    p45 = P45_1_Cheapest_Flight_Within_K_Stops()
    answer = p45.findCheapestPrice(n, flights, src, dst, k)

    print(answer)
