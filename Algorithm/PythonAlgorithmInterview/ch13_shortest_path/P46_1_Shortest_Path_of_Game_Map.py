import collections
import heapq
from typing import List


class P46_1_Shortest_Path_of_Game_Map:

    def solution(self, maps: List[List[int]]):

        pq = [[1, 0, 0]]

        dist = collections.defaultdict(list)

        def dfs(row: int, col: int, distance: int):
            if row < len(maps) and col < len(maps[0]) and row >= 0 and col >= 0 and maps[row][col] == 1:
                maps[row][col] = 0
                heapq.heappush(pq, [distance, row, col])

        while pq:
            node = heapq.heappop(pq)
            node_dist = node[0]
            node_row = node[1]
            node_col = node[2]

            if (1000 * node_row) + node_col not in dist:
                dist[(1000 * node_row) + node_col] = node

                dfs(node_row, node_col + 1, node_dist + 1)
                dfs(node_row + 1, node_col, node_dist + 1)
                dfs(node_row - 1, node_col, node_dist + 1)
                dfs(node_row, node_col - 1, node_dist + 1)

        if (1000 * (len(maps) - 1) + len(maps[0]) - 1) in dist:
            return dist[1000 * (len(maps) - 1) + len(maps[0]) - 1][0]

        return -1
