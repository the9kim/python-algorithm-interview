from typing import List


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    max_fare = 200 * 100000
    opt_fares = [[0 if r == c else max_fare for c in range(n)] for r in range(n)]

    calc_cumulative_sum(n, opt_fares, fares)

    return find_optimal_fare(s - 1, a - 1, b - 1, n, opt_fares)


def calc_cumulative_sum(n: int, opt_fares: List[List[int]], fares: List[List[int]]) -> None:
    for src, dst, fare in fares:
        opt_fares[src - 1][dst - 1] = int(fare)
        opt_fares[dst - 1][src - 1] = int(fare)

    for k in range(n):
        for r in range(n):
            for c in range(n):
                if opt_fares[r][c] > opt_fares[r][k] + opt_fares[k][c]:
                    opt_fares[r][c] = opt_fares[r][k] + opt_fares[k][c]


def find_optimal_fare(s: int, a: int, b: int, n: int, opt_fares: List[List[int]]) -> int:
    min_fare = float('inf')

    for wp in range(n):
        if opt_fares[s][wp] + opt_fares[wp][a] + opt_fares[wp][b] < min_fare:
            min_fare = opt_fares[s][wp] + opt_fares[wp][a] + opt_fares[wp][b]

    return min_fare
