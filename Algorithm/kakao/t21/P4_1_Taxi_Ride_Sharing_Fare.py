from typing import List


class P4_1_Taxi_Ride_Sharing_Fare:
    '''
    1. Create a graph using Ployd-Washall Algorithm
    2. Find the cheapest fare
    '''
    def solution(self, n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
        # 1
        graph = [[200 * 100000 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0

        for start, end, fare in fares:
            graph[start - 1][end - 1] = fare
            graph[end - 1][start - 1] = fare

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]


        # 2
        min_fare = float('inf')
        for i in range(n):
            fare = graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1]
            min_fare = min(min_fare, fare)

        return min_fare