from typing import List


class P4_1_Archery_Tournament:
    def __init__(self, max_sum: int = 0, answer: List[int] = [0] * 11):
        self.max_sum = max_sum
        self.answer = answer

    def solution(self, n: int, info: List[int]) -> List[int]:
        def cal_score(lion: List[int]) -> int:
            total_score = 0

            for i in range(0, 10):
                if lion[i] == info[i]:
                    continue
                elif lion[i] > info[i]:
                    total_score += 10 - i
                else:
                    total_score -= 10 - i

            return total_score

        def dfs(index: int, lion: List[int], arrow: int):
            if index == 11:
                lion[10] = arrow
                total_score = cal_score(lion)
                if total_score > self.max_sum:
                    self.max_sum = total_score
                    self.answer = list(lion)
                elif total_score == self.max_sum:
                    for i in range(10, 0, -1):
                        if self.answer[i] == lion[i]:
                            continue
                        elif self.answer[i] < lion[i]:
                            self.max_sum = total_score
                            self.answer = list(lion)
                        break

                return

            if arrow > info[index]:
                lion[index] = info[index] + 1
                dfs(index + 1, lion, arrow - (info[index] + 1))
                lion[index] = 0

            dfs(index + 1, lion, arrow)

        dfs(0, [0] * 11, n)

        if self.max_sum == 0:
            return [-1]

        return self.answer
