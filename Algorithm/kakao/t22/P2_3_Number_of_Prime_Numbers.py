import math
from collections import deque


def solution(n, k):
    """
    Count the number of prime numbers obtained after converting the given
    integer `n` to base `k` and splitting it by zeros.

    :param n: Integer to convert.
    :param k: Base to convert the integer to.
    :return: Count of prime numbers from split parts.
    """
    # Convert n to base k and split by '0'
    n_base = convert_to_base(n, k)
    split_parts = filter(None, n_base.split("0"))  # Filter out empty strings

    # Count prime numbers in the split parts
    return sum(1 for part in map(int, split_parts) if is_prime(part))


def convert_to_base(n, k):
    """
    Convert a decimal number `n` to a base `k`.

    :param n: Integer to convert.
    :param k: Target base.
    :return: String representation of the number in base `k`.
    """
    n_base = deque()
    while n > 0:
        n_base.appendleft(str(n % k))
        n //= k
    return ''.join(n_base)


def is_prime(num):
    """
    Determine if a number is a prime number.

    :param num: Integer to check.
    :return: True if `num` is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True
