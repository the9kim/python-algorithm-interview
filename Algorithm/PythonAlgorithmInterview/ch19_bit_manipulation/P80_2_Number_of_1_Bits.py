class P80_2_Number_of_1_Bits:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            n &= (n - 1)
            count += 1

        return count