import collections
from typing import List

class P5_1_Merge_Table:
    def solution(self, commands: List[str]) -> List[str]:
        values = [""] * 51 * 51
        neighbors = collections.defaultdict(set)

        answer = []

        for c in commands:
            command = c.split()

            if command[0] == 'UPDATE':
                if len(command) == 4:
                    r, c, v = int(command[1]), int(command[2]), command[3]
                    self.update(r, c, v, values, neighbors)
                else:
                    v1, v2 = command[1], command[2]
                    self.change(v1, v2, values)
            elif command[0] == 'MERGE':
                r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
                self.merge(r1, c1, r2, c2, values, neighbors)

            elif command[0] == 'UNMERGE':
                r1, c1 = int(command[1]), int(command[2])
                self.unmerge(r1, c1, values, neighbors)

            else:
                r1, c1 = int(command[1]), int(command[2])
                answer.append(self.print(r1, c1, values))

        return answer

    def update(self, r, c, v, values, neighbors):
        idx = self.convert_to_idx(r, c)
        if not neighbors[idx]:
            neighbors[idx].add(idx)

        for i in neighbors[idx]:
            values[i] = v
    def change(self, v1, v2, values):
        for i in range(51 * 51):
            if values[i] == v1:
                values[i] = v2

    def merge(self, r1, c1, r2, c2, values, neighbors):
        idx1 = self.convert_to_idx(r1, c1)
        idx2 = self.convert_to_idx(r2, c2)

        # 1. Find the registering value
        value = values[idx1] or values[idx2]

        # 2. Update neighbors and values
        if not neighbors[idx1]:
            neighbors[idx1].add(idx1)
        if not neighbors[idx2]:
            neighbors[idx2].add(idx2)

        new_neighbors = neighbors[idx1].union(neighbors[idx2])

        for i in new_neighbors:
            values[i] = value
            neighbors[i] = new_neighbors

    def unmerge(self, r1, c1, values, neighbors):
        # 1. Find the registering value
        idx = self.convert_to_idx(r1, c1)
        value = values[idx]

        # 2. Initialize neighbors and values
        for i in neighbors[idx]:
            values[i] = ""
            neighbors[i] = set()

        # 3. Update the selected cell
        values[idx] = value
        neighbors[idx].add(idx)

    def print(self, r1, c1, values):
        idx = self.convert_to_idx(r1, c1)
        return values[idx] or "EMPTY"

    def convert_to_idx(self, r, c):
        return r * 51 + c
