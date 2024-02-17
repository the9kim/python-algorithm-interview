import collections
class P31_2_Jewels_and_Stones:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0

        freqs = collections.defaultdict(int);

        for s in stones:
            freqs[s] += 1

        for j in jewels:
            count += freqs[j]

        return count


