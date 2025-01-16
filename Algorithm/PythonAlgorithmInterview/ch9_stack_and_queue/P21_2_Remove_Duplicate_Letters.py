import collections


class P21_2_Remove_Duplicate_Letters:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        processed = set()
        counter = collections.Counter(s)

        for c in s:
            counter[c] -= 1
            if c in processed:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                processed.remove(stack.pop())

            stack.append(c)
            processed.add(c)

        return ''.join(stack)
