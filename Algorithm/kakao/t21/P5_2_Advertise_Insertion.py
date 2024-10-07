from typing import List


def solution(play_time: str, adv_time: str, logs: List[str]) -> str:
    play_time = convert_time_to_sec(play_time)
    adv_time = convert_time_to_sec(adv_time)

    viewing_time = [0 for _ in range(play_time + 1)]
    update_viewing_time(logs, viewing_time, play_time)

    start_time = find_optimal_start_time(viewing_time, play_time, adv_time)

    return format_time(start_time)


def convert_time_to_sec(time: str) -> int:
    h, m, s = map(int, time.split(":"))

    return h * 3600 + m * 60 + s


def update_viewing_time(logs: List[str], viewing_time: List[int], play_time) -> None:
    for log in logs:
        start = convert_time_to_sec(log[:8])
        end = convert_time_to_sec(log[9:])

        viewing_time[start] += 1
        viewing_time[end] -= 1

    for i in range(1, len(viewing_time)):
        viewing_time[i] += viewing_time[i - 1]


def find_optimal_start_time(viewing_time: List[int], play_time: int, adv_time: int) -> int:
    current_sum = sum(viewing_time[i] for i in range(adv_time))
    max_sum = current_sum
    optimal_start_idx = 0

    for i in range(adv_time, play_time):
        current_sum = current_sum + viewing_time[i] - viewing_time[i - adv_time]

        if current_sum > max_sum:
            max_sum = current_sum
            optimal_start_idx = i - adv_time + 1

    return optimal_start_idx


def format_time(start_time):
    return "{:02d}:{:02d}:{:02d}".format(start_time // 3600, start_time % 3600 // 60, start_time % 60)
