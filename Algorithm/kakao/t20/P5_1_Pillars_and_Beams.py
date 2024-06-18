from typing import List

'''
1. Create pillars and beams separately with the condition
2. Remove pillars and beams with the condition
3. Combine Pillars and beams in sorted order.
'''

class P5_1_Pillars_and_Beams:

    def solution(self, n: int, build_frame: List[List[int]]) -> List[List[int]]:
        pillars = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        beams = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        # 1.
        for frame in build_frame:
            x = frame[0]
            y = frame[1]
            shape = frame[2]
            operation = frame[3]

            if operation == 1:
                if shape == 0:
                    if can_pillar(pillars, beams, x, y):
                        pillars[x][y] = True
                else:
                    if can_beam(pillars, beams, x, y):
                        beams[x][y] = True

            else:
                if shape == 0:
                    pillars[x][y] = False
                    if not can_remove(pillars, beams, x, y):
                        pillars[x][y] = True
                else:
                    beams[x][y] = False
                    if not can_remove(pillars, beams, x, y):
                        beams[x][y] = True

        answer = []

        for i in range(n + 1):
            for j in range(n + 1):
                if pillars[i][j] == True:
                    answer.append([i, j, 0])

                if beams[i][j] == True:
                    answer.append([i, j, 1])

        return answer


def can_pillar(pillars, beams, x, y) -> bool:
    if y == 0 or pillars[x][y - 1] == True:
        return True

    if (x > 0 and beams[x - 1][y]) == True or beams[x][y] == True:
        return True

    return False


def can_beam(pillars, beams, x, y):
    if ((y > 0 and pillars[x][y - 1]) == True) or ((y > 0 and x < len(pillars) - 1 and pillars[x + 1][y - 1]) == True):
        return True
    if ((x > 0 and beams[x - 1][y]) == True) and ((x < len(pillars) - 1 and beams[x + 1][y]) == True):
        return True

    return False


def can_remove(pillars, beams, x, y):
    for row in range(max(0, x - 1), x + 2):
        for col in range(y, min(len(pillars[0]) - 1, y + 2)):
            if pillars[row][col] == True and can_pillar(pillars, beams, row, col) == False:
                return False
            if beams[row][col] == True and can_beam(pillars, beams, row, col) == False:
                return False

    return True
