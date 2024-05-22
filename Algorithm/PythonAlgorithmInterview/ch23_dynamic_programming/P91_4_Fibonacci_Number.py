import collections

class P91_4_Fibonacci_Number:
    def fib(self, n: int) -> int:
        x = 0
        y = 1

        for i in range(n):
            z = x + y
            x, y = y, z

        return x