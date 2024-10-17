import math
from collections import defaultdict
from typing import List, Dict


def solution(fees: List[int], records: List[str]):
    time_dict = create_parking_time_dict(records)

    return calculate_fee(fees, time_dict)


def create_parking_time_dict(records: List[str]) -> dict:
    log_dict = {}
    time_dict = defaultdict(int)

    for record in records:
        time, car, status = record.split()

        if status == "IN":
            log_dict[car] = convert_time_to_min(time)
        else:
            duration = convert_time_to_min(time) - log_dict[car]
            time_dict[car] += duration
            log_dict.pop(car)

    for car in log_dict.keys():
        duration = 1439 - log_dict[car]
        time_dict[car] += duration

    return time_dict


def calculate_fee(fees: List[int], time_dict: Dict[str, int]) -> List[int]:
    basic_time, basic_fare, unit_time, unit_fare = fees[0], fees[1], fees[2], fees[3]

    fares = []

    sorted_keys = sorted(list(time_dict.keys()))

    for key in sorted_keys:
        if time_dict[key] < basic_time:
            fares.append(basic_fare)
        else:
            fare = basic_fare + math.ceil((time_dict[key] - basic_time) / unit_time) * unit_fare
            fares.append(fare)

    return fares


def convert_time_to_min(time: str) -> int:
    h, m = time.split(":")
    return int(h) * 60 + int(m)
