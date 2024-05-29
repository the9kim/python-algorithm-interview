class P1_1_Dart_Game:
    def solution(self, dartResult: str) -> int:
        score = [0]

        for i, n in enumerate(dartResult):
            if n == "S":
                score.append(0)
            elif n == "D":
                score[-1] **= 2
                score.append(0)
            elif n == "T":
                score[-1] **= 3
                score.append(0)
            elif n == "*":
                if len(score) > 2:
                    score[-3] *= 2
                score[-2] *= 2
            elif n == "#":
                score[-2] *= -1
            else:
                score[-1] = score[-1] * 10 + int(n)

        return sum(score)











