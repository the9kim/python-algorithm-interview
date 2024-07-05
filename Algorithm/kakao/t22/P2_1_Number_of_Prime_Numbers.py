import math


class P2_1_Number_of_Prime_Numbers:

    '''
    1. Convert the input number to base-k number
    2. Count the number of Prime Numbers that match the condition
    '''
    def solution(self, n: int, k: int) -> int:
        # 1.
        stack = []

        while n != 0:
            remainder = n % k
            stack.append(remainder)
            n //= k

        k_base = ""
        while stack:
            k_base += str(stack.pop())

        # 2.
        count = 0
        for n in k_base.split("0"):
            if n == '':
                continue

            if self.is_prime_number(int(n)):
                count += 1

        return count
    def is_prime_number(self, n: int) -> bool:
        if n <= 1 or (n > 2 and n % 2 == 0):
            return False
        for i in range(3, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True



