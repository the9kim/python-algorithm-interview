import datetime
from typing import List


class P7_1_Thankgiving_Traffic:
    '''
    1. Convert logs to 'TimeStamp', capturing both request time and response time
    2. Sort the list of request and response time in ascending order
    3. Determine the maximum requests per second
    '''

    def solution(self, lines: List[str]) -> int:
        # 1.
        logs = []

        for line in lines:
            date, time, duration = line.split(" ")
            timestamp = datetime.datetime.strptime(date + ' ' + time, "%Y-%m-%d %H:%M:%S.%f").timestamp()
            logs.append((timestamp, -1))
            logs.append((timestamp - float(duration[:-1]) + 0.001, 1))

        # 2.
        logs.sort(key=lambda x: x[0])

        # 3.
        accumulated = 0
        max_request = 1
        for i, elem1 in enumerate(logs):
            current = accumulated

            for elem2 in logs[i:]:

                if elem2[0] - elem1[0] > 0.999:
                    break
                if elem2[1] > 0:
                    current += elem2[1]

            max_request = max(max_request, current)
            accumulated += elem1[1]

        return max_request
