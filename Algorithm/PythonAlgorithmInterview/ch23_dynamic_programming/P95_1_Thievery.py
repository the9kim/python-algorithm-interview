from typing import List


class P95_1_Thievery:
    def solution(self, money: List[int]) -> int:

        answer = []

        answer.append([0, 0])
        answer.append([0, money[1]])

        for i in range(2, len(money)):
            answer[0].append(max(answer[0][i - 1], answer[0][i -2] + money[i]))
            answer[1].append(max(answer[1][i - 1], answer[1][i - 2] + money[i]))

        return max(answer[0][-2] + money[0], answer[1][-1])




