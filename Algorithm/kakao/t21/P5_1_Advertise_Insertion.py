from typing import List


class P5_1_Advertise_Insertion:
    '''
    1. Calculate accumulated playing time using a list
    2. Find the starting time to maximize ad exposure using sliding window technique
    '''

    def solution(self, play_time: str, adv_time: str, logs: List[str]) -> str:
        play_sec_time = self.convertToSec(play_time)
        adv_sec_time = self.convertToSec(adv_time)

        # 1.
        playing = [0 for _ in range(play_sec_time + 1)]

        for log in logs:
            s_log, e_log = log.split("-")
            start = self.convertToSec(s_log)
            end = self.convertToSec(e_log)

            playing[start] += 1
            playing[end] -= 1

        for i in range(1, play_sec_time):
            playing[i] += playing[i - 1]

        # 2.
        sum_time = sum(playing[:adv_sec_time])

        max_time = sum_time
        start_time = 0

        for i in range(adv_sec_time, play_sec_time):
            sum_time = sum_time - playing[i - adv_sec_time] + playing[i]
            if sum_time > max_time:
                max_time = sum_time
                start_time = i - adv_sec_time + 1

        return "%02d:%02d:%02d" % (start_time // 3600, start_time % 3600 // 60, start_time % 60)

    def convertToSec(self, time: str) -> int:
        h, m, s = time.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
