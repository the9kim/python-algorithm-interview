from collections import defaultdict
from typing import List


def solution(id_list: List[int], report: List[str], k: int) -> List[int]:
    report = set(report)

    reported_map = defaultdict(list)
    update_report_map(report, reported_map)

    email_count = defaultdict(int)
    update_email_count(email_count, k, reported_map)

    return find_result(email_count, id_list)


def find_result(email_count, id_list):
    result = []
    for id in id_list:
        result.append(email_count[id])
    return result


def update_email_count(email_count, k, reported_map):
    for reported, reportings in reported_map.items():
        if len(reportings) >= k:
            for reporting in reportings:
                email_count[reporting] += 1


def update_report_map(report, reported_map):
    for r in report:
        reporting, reported = r.split(" ")
        reported_map[reported].append(reporting)
