import collections
class P32_1_Longest_Substring_Without_Duplicating_Characters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = collections.defaultdict(int)

        left = 0
        right = 0
        length = 0

        for i, c in enumerate(s):
            if c in used and used[c] >= left:
                left = used[c] + 1
            length = max(length, right - left + 1)
            used[c] = i
            right += 1

        return length

