from typing import List
import collections

class P42_1_Course_Schedule:
    def canFinish(self, numsCourses: int, prerequisites: List[List[int]]) -> bool:

        # 1. Create a graph
        graph = collections.defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])

        route = []
        taken = []

        def dfs(end: int) -> bool:
            if end in route:
                return False
            if end in taken:
                return True

            if end in graph:
                route.append(end)
                for pre in graph[end]:
                    if not dfs(pre):
                        return False

                route.remove(end)
                taken.append(end)

            return True



        # 2. Check cyclic composition

        for end in graph:
            if not dfs(end):
                return False

        return True




if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]

    p42 = P42_1_Course_Schedule()
    answer = p42.canFinish(numCourses, prerequisites)

    print(answer)
