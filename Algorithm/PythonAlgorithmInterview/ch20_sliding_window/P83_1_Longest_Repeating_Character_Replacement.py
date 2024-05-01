import collections

class P83_1_Longest_Repeating_Character_Replacement:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        counter = collections.defaultdict(int)

        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            most_freq = max(counter.values())

            if (right - left - most_freq) > k:
                counter[s[left]] -= 1
                left += 1

        return len(s) - left



