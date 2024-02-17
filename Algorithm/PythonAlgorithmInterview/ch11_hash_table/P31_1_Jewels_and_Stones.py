class P31_1_Jewels_and_Stones:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0

        freqs = {}

        for s in stones:
            if s not in freqs:
                freqs[s] = 1
            else:
                freqs[s] += 1

        for j in jewels:
            if j in freqs:
                count += freqs[j]

        return count

