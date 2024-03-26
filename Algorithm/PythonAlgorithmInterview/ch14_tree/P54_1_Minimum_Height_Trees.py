from typing import List
import collections

class P54_1_Minumum_Height_Tree:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = collections.defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:

            n -= len(leaves)

            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf][0]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves


        return leaves


if __name__ == '__main__':
    edges = [[1, 0], [1, 2], [1, 3]]
    n = 4

    p54 = P54_1_Minumum_Height_Tree()
    MHT = p54.findMinHeightTrees(n, edges)
    print(MHT)


