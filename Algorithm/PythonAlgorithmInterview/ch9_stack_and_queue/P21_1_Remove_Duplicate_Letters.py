import collections


class P21_1_Remove_Duplicate_Letters:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)
        verifier = collections.defaultdict(bool)

        for val in s:

            counter[val] -= 1

            if verifier[val] == True:
                continue

            while stack and stack[-1] > val and counter[stack[-1]] > 0:
                verifier[stack.pop()] = False

            stack.append(val)
            verifier[val] = True

        answer = ''

        for s in stack:
            answer += s

        return answer

