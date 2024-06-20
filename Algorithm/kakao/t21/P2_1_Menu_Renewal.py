from typing import List
import collections

class P2_1_Menu_Renewal:
    '''
    1. Set data structures
    2. Calculate combinations based on the length of words and store them into a dictionary
    3. Check if the value of the dictionary is more than 2 and make the answer
    '''
    def solution(self, orders: List[str], course: List[int]) -> List[str]:

        # 1
        combinations = []
        for i in range(0, 10):
            combinations.append(collections.defaultdict(int))
        max_count = [0] * 10

        # 2.
        for size in course:
            for order in orders:
                if len(order) >= size:
                    self.calculate_combination(combinations, max_count, ''.join(sorted(order)), size, "", 0)

        # 3
        answer = []
        for i, size in enumerate(course):
            for key in combinations[size - 2]:
                if combinations[size - 2][key] >= 2 \
                    and combinations[size - 2][key] == max_count[size - 2]:
                    answer.append(key)

        return sorted(answer)



    def calculate_combination(self, combinations, max_count, order, size, elem, index):
        if len(elem) == size:
            combinations[size - 2][elem] += 1
            max_count[size - 2] = max(max_count[size - 2], combinations[size - 2][elem])
            return

        for i in range(index, len(order)):
            elem += order[i]
            self.calculate_combination(combinations, max_count, order, size, elem, i + 1)
            elem = elem[:-1]





