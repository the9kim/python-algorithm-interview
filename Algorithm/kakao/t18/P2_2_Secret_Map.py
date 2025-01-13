from typing import List


class P2_2_Secret_Map:
    def solution(self, n:int, arr1:List[str], arr2:List[str])-> list[str]:
        return [
            f"{bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' '):>{n}}" \
            for i in range(n)
        ]