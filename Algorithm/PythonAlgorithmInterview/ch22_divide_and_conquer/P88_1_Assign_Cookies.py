from typing import List


class P88_1_Assign_Cookies:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 1. Sort input Arrays
        g = sorted(g)
        s = sorted(s)

        # 2. Move each pointer
        g_idx = 0
        s_idx = 0

        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                g_idx += 1

            s_idx += 1

        return g_idx