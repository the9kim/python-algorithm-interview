from typing import List
import collections


class P7_1_Minimizaing_Sales_Decline:
    '''
    1. Create a graph
    2. Calculate the optimal cumulative sum using DP and DFS
    '''

    def solution(self, sales: List[int], links: List[List[int]]):
        # 1.
        graph = collections.defaultdict(list)
        for src, dst in links:
            graph[src - 1].append(dst - 1)

        # 2.
        N = len(sales)
        expense = [[0, 0] for _ in range(N)]

        def dfs(node: int) -> None:
            expense[node][0] = 0
            expense[node][1] = sales[node]

            if not graph[node]:
                return

            min_node = float('inf')
            for next in graph[node]:
                dfs(next)

                if expense[next][0] < expense[next][1]:
                    expense[node][0] += expense[next][0]
                    expense[node][1] += expense[next][0]
                    min_node = min(min_node, expense[next][1] - expense[next][0])
                else:
                    expense[node][0] += expense[next][1]
                    expense[node][1] += expense[next][1]
                    min_node = 0

            expense[node][0] += min_node

        dfs(0)

        return min(expense[0][0], expense[0][1])
