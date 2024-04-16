from typing import List


class P67_1_Largest_Number:
    def largestNumber(self, nums: List[int]) -> str:

        @staticmethod
        def can_swap(n1: int, n2: int) -> bool:
            return str(n2) + str(n1) > str(n1) + str(n2)

        i = 1

        while i < len(nums):
            j = i
            while j > 0 and can_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1

        answer = ''.join(map(str, nums))

        if answer.startswith('0'):
            return '0'

        return answer