from typing import List
import collections

class P7_1_Dropping_Numbers:
    '''
    1. Create a graph
    2. Find the minimum count of cards
    3. Find the smallest number for each card
    '''
    def solution(self, edges: List[List[int]], target: List[int]) -> List[int]:
        N = len(edges) + 1
        T = 0

        # 1.
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src - 1].append(dst - 1)

        for key, value in graph.items():
            graph[key] = sorted(value)

        # 2.
        visit_count = [0] * N
        num_count = [0] * N
        checked = [False] * N
        leaves = []

        for n in range(N):
            if not graph[n] and target[n] > 0:
                T += 1

        while T > 0:
            node = 0
            while graph[node]:
                idx = visit_count[node] % len(graph[node])
                visit_count[node] += 1
                node = graph[node][idx]


            num_count[node] += 1
            leaves.append(node)

            if num_count[node] > target[node]:
                return [-1]

            if not checked[node] and num_count[node] * 3 >= target[node]:
                checked[node] = True
                T -= 1

        # 3.
        answer = []

        for leaf in leaves:
            num_count[leaf] -= 1
            for n in range(1, 4):
                if num_count[leaf] <= target[leaf] - n and num_count[leaf] * 3 >= target[leaf] - n:
                    answer.append(n)
                    target[leaf] -= n
                    break

        return answer

