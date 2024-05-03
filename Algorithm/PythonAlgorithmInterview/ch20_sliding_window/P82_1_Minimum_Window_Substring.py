import collections


class P82_1_Minimum_Window_Substring:
    def minWindow(self, s: str, t: str) -> str:

        # 1
        dict = collections.defaultdict(int)
        for c in t:
            dict[c] += 1

        left, right = 0, 0
        start, end = 0, 0

        window = len(t)
        min = float('inf')
        for c in s:
            # 2
            right += 1

            if dict[c] and dict[c] > 0:
                window -= 1

            dict[c] -= 1

            # 3.
            if window == 0:
                while dict[s[left]] and dict[s[left]] < 0:
                    dict[s[left]] += 1
                    left += 1

                if right - left + 1 < min:
                    min = right - left + 1
                    start, end = left, right

                dict[s[left]] += 1
                left += 1
                window += 1

        return s[start: end]
