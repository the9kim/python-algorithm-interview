import collections


class P78_1_Sum_of_Two_Integer:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MASK = 0x7FFFFFFF

        bin_a = bin(a & MASK)[2:].zfill(32)
        bin_b = bin(b & MASK)[2:].zfill(32)

        sum = collections.deque()
        carry_out = 0

        for i in range(0, 32):
            i1 = int(bin_a[31 - i])
            i2 = int(bin_b[31 - i])

            sum_1 = i1 ^ i2
            sum_2 = carry_out ^ sum_1
            sum.appendleft(str(sum_2))

            carry_1 = i1 & i2
            carry_2 = sum_1 & carry_out
            carry_out = carry_1 | carry_2

        if carry_out == 1:
            sum.appendleft(str(carry_out))

        result = int(''.join(sum), 2) & MASK

        if result > INT_MASK:
            result = ~(result ^ MASK)

        return result