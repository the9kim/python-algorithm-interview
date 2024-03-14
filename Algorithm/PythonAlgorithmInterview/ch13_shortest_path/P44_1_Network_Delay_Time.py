import heapq
from typing import List
import collections


class P44_1_Network_Delay_Time:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append([v, w])



        pq = [[0, k]]
        dist = collections.defaultdict(int)

        heapq.heappush(pq, [0, k])

        while pq:
            nodeTime, nodeId = heapq.heappop(pq)


            if nodeId not in dist:
                dist[nodeId] = nodeTime

                for nextNode, nextTime in graph[nodeId]:
                    newTime = nodeTime + nextTime
                    heapq.heappush(pq, [newTime, nextNode])



        if len(dist) == n:
            return max(dist.values())

        return -1


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2

    p44 = P44_1_Network_Delay_Time()
    answer = p44.networkDelayTime(times, n, k)

    print(answer)





