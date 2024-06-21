from typing import List
import collections
import bisect


class P3_1_Rank_Search:
    '''
    1. Classify the input information into 108 possible cases using a list
    2. Sort the list in ascending order
    3. Find the number of elements that meets conditions in each query using a binary search
    '''

    def solution(self, info: List[str], query: List[str]) -> List[int]:
        # 1
        graph = [[] for i in range(4 * 3 * 3 * 3)]
        word_map = collections.defaultdict(int)
        word_map['-'] = 0
        word_map['cpp'] = 1
        word_map['java'] = 2
        word_map['python'] = 3
        word_map['backend'] = 1
        word_map['frontend'] = 2
        word_map['junior'] = 1
        word_map['senior'] = 2
        word_map['chicken'] = 1
        word_map['pizza'] = 2

        for n in info:
            info_list = n.split()
            info_idx = [
                word_map[info_list[0]] * 3 * 3 * 3,
                word_map[info_list[1]] * 3 * 3,
                word_map[info_list[2]] * 3,
                word_map[info_list[3]]
            ]
            score = int(info_list[4])

            for i in range(1 << 4):
                idx = 0
                for j in range(4):
                    if (i & (1 << j) != 0):
                        idx += info_idx[j]
                graph[idx].append(score)

        # 2.
        for i in range(0, 4 * 3 * 3 * 3):
            graph[i] = sorted(graph[i])

        # 3.
        answer = []

        for q in query:
            q_list = q.split()
            idx = word_map[q_list[0]] * 3 * 3 * 3 \
                  + word_map[q_list[2]] * 3 * 3 \
                  + word_map[q_list[4]] * 3 \
                  + word_map[q_list[6]]
            score = int(q_list[7])

            ret = bisect.bisect_left(graph[idx], score)

            answer.append(len(graph[idx]) - ret)

        return answer