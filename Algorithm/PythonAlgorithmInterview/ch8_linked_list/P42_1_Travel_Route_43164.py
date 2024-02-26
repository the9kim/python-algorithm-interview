import heapq
from typing import List
import collections

class P42_1_Travel_Route_43164:
    def solution(self, tickets: List[List[str]]) -> List[str]:

        # 1. Create a graph
        graph = collections.defaultdict(list)

        for ticket in tickets:
            heapq.heappush(graph[ticket[0]], ticket[1])


        # 2. Find a route
        stack = list()
        route = list()

        stack.append('ICN')
        while stack:
            while graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]]))
            route.append(stack.pop())
        return route[::-1]



