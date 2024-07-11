from typing import List
import collections
class Node:
    def __init__(self, index: int, sheep: int, wolves: int, nodes: List[int]):
        self.index = index
        self.sheep = sheep
        self.wolves = wolves
        self.nodes = nodes
class P5_1_Sheep_and_Wovles:

    '''
    1. Create a Graph and Node class
    2. Find the maximum number of sheep using iterative BFS
    '''
    def solution(self, info: List[int], edges: List[List[int]]) -> int:

        # 1.
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])

        # 2.
        max_sheep = 1

        q = [Node(0, 1, 0, graph.get(0))]

        while q:
            node = q.pop()

            for child in node.nodes:
                next_sheep = node.sheep + 1 if info[child] == 0 else node.sheep
                next_wolves = node.wolves + 1 if info[child] == 1 else node.wolves

                if next_sheep > next_wolves:
                    max_sheep = max(max_sheep, next_sheep)
                    new_children = list(node.nodes)
                    new_children.remove(child)
                    if graph[child]:
                        new_children.extend(graph[child])
                    q.append(Node(child, next_sheep, next_wolves, new_children))

        return max_sheep