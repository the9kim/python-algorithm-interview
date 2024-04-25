class P77_1_Hamming_Distance:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')