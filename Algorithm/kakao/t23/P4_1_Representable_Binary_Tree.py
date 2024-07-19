from typing import List
class P4_1_Representable_Binary_Tree:

    '''
    1. Convert the input number to binary numbers
    2. Add padding to the binary number to align it with a Full Binary Tree
    3. Check If the binary numbers are representable as a Full Binary Tree
    '''
    def solution(self, numbers: List[int]) -> List[int]:

        answer = []

        for num in numbers:
            # 1.
            bin_num = bin(num)[2:]

            # 2.
            h, n = 0, 1
            while len(bin_num) > n:
                h += 1
                n += 2 ** h

            padding = '0' * (n - len(bin_num))
            bin_num = padding + bin_num

            # 3.
            def deserialize(left: int, right: int, dummy: bool) -> bool:
                if left == right and dummy and bin_num[left] == '1':
                    return False
                elif left == right:
                    return True

                mid = left + (right - left) // 2

                if dummy == True and bin_num[mid] == '1':
                    return False

                dummy = dummy or bin_num[mid] == '0'

                return deserialize(left, mid - 1, dummy) and deserialize(mid + 1, right, dummy)

            answer.append(int(deserialize(0, len(bin_num) - 1, False)))

        return answer



