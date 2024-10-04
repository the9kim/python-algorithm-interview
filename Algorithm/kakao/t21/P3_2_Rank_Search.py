import bisect
import re
from typing import Dict, List


def solution(info: List[str], query: List[str]) -> List[int]:
    scores = create_score_list()
    index_map = setup_data()

    process_info(info, scores, index_map)

    sort_scores(scores)

    return process_queries(query, scores, index_map)


def create_score_list():
    scores = [[] for _ in range(4 * 3 * 3 * 3)]
    return scores


def setup_data() -> Dict[str, int]:
    return {
        '-': 0,
        'cpp': 1,
        'java': 2,
        'python': 3,
        'backend': 1,
        'frontend': 2,
        'junior': 1,
        'senior': 2,
        'chicken': 1,
        'pizza': 2
    }


def process_info(info: List[str], scores: List[List[int]], index_map: Dict) -> None:
    for data in info:
        lang, job, pos, food, score = data.split()
        indices = [
            index_map[lang] * 3 * 3 * 3,
            index_map[job] * 3 * 3,
            index_map[pos] * 3,
            index_map[food]
        ]
        score = int(score)

        add_scores_to_combinations(indices, scores, score)


def add_scores_to_combinations(indices: List[int], scores: List[List[int]], score: int):
    for i in range(1 << 4):
        index = sum(indices[j] if (i & (1 << j)) != 0 else 0 for j in range(4))
        scores[index].append(score)


def sort_scores(scores: List[List[int]]) -> None:
    for score in scores:
        score.sort()


def process_queries(query: List[str], scores: List[List[int]], index_map: dict) -> List[int]:
    results = []

    for q in query:
        q = q.replace("and", "")
        q = re.sub("\\s+", " ", q)
        lang, job, pos, food, target_score = q.split()
        target_score = int(target_score)
        index = index_map[lang] * 3 * 3 * 3 \
                + index_map[job] * 3 * 3 \
                + index_map[pos] * 3 \
                + index_map[food]

        scores_to_lookup = scores[index]
        count = len(scores_to_lookup) - bisect.bisect_left(scores_to_lookup, target_score)
        results.append(count)

    return results
