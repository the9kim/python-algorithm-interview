class P80_1_Number_of_1_Bits:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')