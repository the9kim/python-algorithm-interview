from typing import List

class P6_1_Shuttle_Bus:
    '''
    1. Convert the input timetable to minutes
    2. Sort the timetable in ascending order
    3. Sequentially board crews onto the bus and determine the waiting time in line
    '''
    def solution(self, n: int, t: int, m: int, timetable: List[str]) -> str:
        def convert_time_to_min(time: str) -> int:
            h, m  = time.split(":")
            return int(h) * 60 + int(m)
        def convert_min_to_time(time :int) -> str:
            return "%02d:%02d" % (time // 60, time % 60)

        # 1.
        crews = []
        for time in timetable:
            crews.append(convert_time_to_min(time))


        # 2.
        crews = sorted(crews)

        # 3.
        departing_time = 9 * 60
        waiting_time = -1

        for bus in range(n):
            for seat in range(m):

                if crews and crews[0] <= departing_time:
                    crew = crews.pop(0)
                    waiting_time = crew - 1
                else:
                    waiting_time = departing_time

            departing_time += t

        return convert_min_to_time(waiting_time)


