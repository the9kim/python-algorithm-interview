from collections import defaultdict
from typing import List


def solution(id_list: List[int], report: List[str], k: int) -> List[int]:
    report_pairs = {tuple(r.split()) for r in report}

    reported = defaultdict(set)

    for reporter, reported_person in report_pairs:
        reported[reported_person].add(reporter)

    email_count = defaultdict(int)

    for reported_person, reporters in reported.items():
        if len(reporters) >= k:
            for reporter in reporters:
                email_count[reporter] += 1

    return [email_count[user] for user in id_list]



