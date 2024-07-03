import collections
from typing import List


class P1_1_Report_Result:
    '''
    1. Create a dictionary to contains reporting individuals as value and a reported individual as a key
    2. Check the number of reporting people for an individual and Update the frequency of getting emails
    '''
    def solution(self, id_list: List[str], report: List[str], k :int) -> List[int]:
        # 1
        report = set(report)
        report_map = collections.defaultdict(list)
        for r in report:
            reporting, reported = r.split()
            report_map[reported].append(reporting)

        # 2.
        counter = collections.defaultdict(int)
        for reported, reportings in report_map.items():
            if len(reportings) >= k:
                for reporting in reportings:
                    counter[reporting] += 1

        # 3.
        answer = []
        for id in id_list:
            answer.append(counter[id])

        return answer
