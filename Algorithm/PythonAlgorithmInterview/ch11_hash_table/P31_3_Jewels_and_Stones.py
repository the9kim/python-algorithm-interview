import collections
class P31_3_Jewels_and_Stones:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)

        result = 0

        for j in jewels:
            result += counter[j]

        return result

