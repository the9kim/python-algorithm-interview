from typing import List

class Node:
    def __init__(self):
        self.value = "EMPTY"
        self.merged = [self]
def solution(commands: List[str]) -> List[str]:
    table = [[Node() for _ in range(0, 51)] for _ in range(0, 51)]

    results = []

    for command in commands:
        c = command.split()

        if c[0] == 'UPDATE':
            if len(c) == 4:
                row = int(c[1])
                col = int(c[2])
                value = c[3]

                for node in table[row][col].merged:
                    node.value = value

            else:
                target = c[1]
                new_value = c[2]

                for row in range(1, 50):
                    for col in range(1, 50):
                        if table[row][col].value == target:
                            table[row][col].value = new_value


        elif c[0] == 'MERGE':
            r1 = int(c[1])
            c1 = int(c[2])
            r2 = int(c[3])
            c2 = int(c[4])

            new_value = table[r1][c1].value if table[r1][c1].value != 'EMPTY' else table[r2][c2].value

            new_merged = []
            new_merged.extend(table[r1][c1].merged)
            new_merged.extend(table[r2][c2].merged)

            for node in set(new_merged):
                node.value = new_value
                node.merged = new_merged


        elif c[0] == 'UNMERGE':
            row = int(c[1])
            col = int(c[2])

            remaining = table[row][col].value

            

        else:
            row = int(c[1])
            col = int(c[2])
            results.append(table[row][col].value)

    return results

