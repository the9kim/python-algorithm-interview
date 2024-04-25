class P77_1_Hamming_Distance:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1. Calculate XOR between the two input integers
        xor = x ^ y

        # 2. Count the number of 1
        count = 0

        while xor != 0:
            count += xor & 1
            xor >>= 1

        return count