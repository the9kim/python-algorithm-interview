from typing import List
import collections


class P81_Sliding_Window_Maximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       answer = []
       window = collections.deque()

       max_value = float('-inf')

       for i, n in enumerate(nums):
           window.append(n)

           if i < k - 1:
               continue

           if max_value == float('-inf'):
               max_value = max(window)
           elif n > max_value:
               max_value = n

           answer.append(max_value)

           if window.popleft() == max_value:
               max_value = float('-inf')

       return answer


