import heapq
from typing import List
import collections


class P41_1_Reconstruct_Itinerary:
    def findItineraray(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for ticket in tickets:
            heapq.heappush(graph[ticket[0]], ticket[1])


        stack = []
        stack.append("JFK")
        answer = collections.deque()

        while stack:
            while graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]]))

            answer.appendleft(stack.pop())


        return list(answer)


if __name__ == '__main__':
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    p41 = P41_1_Reconstruct_Itinerary()
    answer = p41.findItineraray(tickets)

    print(answer)