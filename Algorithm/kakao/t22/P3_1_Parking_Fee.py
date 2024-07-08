from typing import List
import collections
import math


class P3_1_Parking_Fee:

    '''
    1. Calculate total parking time for each car
    2. Calculate total parking fee for each car
    '''
    def solution(self, fees: List[int], records: List[str]) -> List[int]:
        # 1.
        parking_log = collections.defaultdict(int)
        parking_time = collections.defaultdict(int)

        for record in records:
            log = record.split()
            time = log[0].split(":")
            car = log[1]
            in_or_out = log[2]

            if in_or_out == 'IN':
                parking_log[car] = int(time[0]) * 60 + int(time[1])
            else :
                parking_time[car] += int(time[0]) * 60 + int(time[1]) - parking_log[car]
                parking_log.pop(car)

        for key, value in parking_log.items():
            parking_time[key] += 1439 - value

        # 2.
        cars = sorted(parking_time.keys())
        answer = []

        basic_time = fees[0]
        basic_fee = fees[1]
        add_time = fees[2]
        add_fee = fees[3]

        for car in cars:
            total_time = parking_time[car]
            if total_time <= basic_time:
                answer.append(basic_fee)
            else:
                answer.append(basic_fee + math.ceil((total_time - basic_time) / add_time) * add_fee)

        return answer