from typing import List


class P87_1_Gas_Station:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        fuel = 0

        for i in range(len(gas)):
            if gas[i] - cost[i] + fuel < 0:
                start = i + 1
                fuel = 0

            else:
                fuel += gas[i] - cost[i]

        return start
