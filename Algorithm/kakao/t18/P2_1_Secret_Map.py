from typing import List


class P2_1_Seecret_Map:
    def solution(self, n:int, arr1:List[str], arr2:List[str])-> int:

        answer = []

        for i in range(n):
            # 1. Utilize OR operation
            binary = bin(arr1[i] | arr2[i])

            # 2. Convert binary representation to the symbols
            binary = binary[2:].zfill(n).replace('1', '#').replace('0', ' ')
            answer.append(binary)

        return answer