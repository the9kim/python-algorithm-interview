from typing import List

class Food:
    def __init__(self, idx: int, time: int) :
        self.idx = idx
        self.time = time

class P4_1_Muji_Live:
    '''
    1. Convert to the elements in the input list to objects and sort them in order as time values
    2. Calculate the difference between the current index and the previous index in the list, multiply that difference by the length from the current index to the end of the list, and then subtract the resulting value from k.
    3. Sort the input list in ascending order as index and Find the target index
    '''
    def solution(self, food_times: List[int], k: int) -> int:
        # 1.
        foods = []
        for i, n in enumerate(food_times):
            foods.append(Food(i + 1, n))

        foods = sorted(foods, key=lambda x: x.time)

        # 2.
        prev_time = 0
        n = len(food_times)

        for i, food in enumerate(foods):
            diff = food.time - prev_time

            if diff > 0:
                square = diff * n
                if square <= k:
                    k -= square
                    prev_time = food.time
                else:
                    # 3.
                    k %= n
                    return sorted(foods[i:], key=lambda x : x.idx)[k].idx

            n -= 1

        return -1