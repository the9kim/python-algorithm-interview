from typing import List

max_score = 0
optimal_shots = [0] * 11


def solution(n: int, info: List[int]) -> List[int]:
    dfs(info, [0] * 11, n, 0)

    return [-1] if max_score == 0 else optimal_shots


def dfs(info: List[int], lion: List[int], n: int, idx: int):
    global max_score, optimal_shots

    if idx == 11:
        lion[10] = n

        score = calc_score(info, lion)

        if score > max_score:
            max_score = score
            optimal_shots = list(lion)
        elif score == max_score:
            for i in range(10, -1, -1):
                if optimal_shots[i] == lion[i]:
                    continue
                if optimal_shots[i] < lion[i]:
                    optimal_shots = list(lion)
                break
        return

    if info[idx] < n:
        lion[idx] = info[idx] + 1
        dfs(info, lion, n - lion[idx], idx + 1)
        lion[idx] = 0

    dfs(info, lion, n, idx + 1)


def calc_score(info: List[int], lion: List[int]) -> int:
    score = 0

    for i in range(0, 11):
        if info[i] == 0 and lion[i] == 0:
            continue

        if info[i] < lion[i]:
            score += (10 - i)
        else:
            score -= (10 - i)

    return score
