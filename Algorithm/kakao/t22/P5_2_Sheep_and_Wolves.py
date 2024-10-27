from typing import List
from collections import defaultdict
from collections import deque

max_sheep = 1

def solution(info: List[int], edges: List[List[int]]) -> int:
    graph = create_graph(edges)

    update_max_sheep(info, graph)

    return max_sheep
def create_graph(edges: List[List[int]]) -> defaultdict:

    graph = defaultdict(list)

    for src, dst in edges:
        graph[src].append(dst)

    return graph


def update_max_sheep(info: List[int], graph: defaultdict) -> None:
    global max_sheep

    q = deque()
    q.append((0, 1, 0, graph[0]))

    while q:
        idx, sheep, wolves, children = q.popleft()

        for child in children:
            next_sheep = sheep + (1 if info[child] == 0 else 0)
            next_wolves = wolves + (1 if info[child] == 1 else 0)

            if next_sheep > next_wolves:
                max_sheep = max(max_sheep, next_sheep)

                next_children = list(children)
                next_children.remove(child)

                if child in graph:
                    next_children.extend(graph[child])

                q.append((child, next_sheep, next_wolves, next_children))








