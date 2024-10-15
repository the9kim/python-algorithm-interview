import math
import re


def solution(n: int, k: int) -> int:
    base = calc_base_number(n, k)

    return count_prime_numbers(base)


def calc_base_number(n: int, k: int) -> str:
    stack = []

    while n != 0:
        remainder = n % k
        stack.append(remainder)
        n //= k

    k_base = ""

    while stack:
        k_base += str(stack.pop())

    return k_base


def count_prime_numbers(base: str) -> int:
    count = 0

    for n in re.split('0+', base):
        if is_prime_number(int(n)):
            count += 1

    for n in base.split('0'):
        if n == '':
            continue

        if is_prime_number(int(n)):
            count += 1

    return count


def is_prime_number(num: int) -> bool:
    if num <= 1 or (num != 2 and num % 2 == 0):
        return False

    for divisor in range(3, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False

    return True
