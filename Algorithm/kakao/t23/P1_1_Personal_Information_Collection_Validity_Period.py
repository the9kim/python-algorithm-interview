from typing import List


class P1_1_Personal_Information_Collection_Validity_Period:
    '''
    1. Convert dates to days and create a terms map
    2. Calculate validity period and compare it with today value
    '''

    def solution(self, today: str, terms: List[str], privacies: List[List[str]]) -> List[int]:
        # 1.
        terms_map = {}
        for t in terms:
            term, period = t.split()
            terms_map[term] = int(period) * 28

        # 2.
        answer = []
        t_day = self.convert_to_day(today)
        for i, p in enumerate(privacies):
            date, term = p.split()
            crnt_day = self.convert_to_day(date) + terms_map[term] - 1

            if t_day > crnt_day:
                answer.append(i + 1)

        return answer

    def convert_to_day(self, date: str) -> int:
        year, month, day = date.split(".")
        return int(year[2:4]) * 12 * 28 + int(month) * 28 + int(day)
