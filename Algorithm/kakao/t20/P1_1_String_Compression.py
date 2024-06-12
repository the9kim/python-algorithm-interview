import collections


class P1_1_String_Compression:
    '''
    1. Utilize iteration for sizes of unit
    2. Utilize iteration for each unit in the input string and check repeated units
    3. Compress the repeated units
    4. Check and update the compressed size of the input string
    '''

    def solution(self, s):
        min_len = len(s)

        # 1.
        for size in range(1, len(s)):
            counter = collections.defaultdict(int)
            prev = ""
            answer = ""
            idx = 0

            # 2.
            for i in range(0, len(s) - size + 1, size):
                unit = s[i:i + size]
                idx = i + size

                # 3
                if unit != prev:
                    if prev != "":
                        if counter[prev] > 1:
                            answer += str(counter[prev])
                        answer += str(prev)
                        counter[prev] = 0

                counter[unit] += 1
                prev = unit

            if counter[prev] > 1:
                answer += str(counter[prev])
            answer += str(prev)
            answer += s[idx:]

            min_len = min(min_len, len(answer))

        return min_len