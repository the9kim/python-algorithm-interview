from typing import List
import collections


class P81_Sliding_Window_Maximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       answer = []
       window = collections.deque()

       for i, n in enumerate(nums):

           if window and window[0] < i - k + 1:
               window.popleft()

           while window and nums[window[-1]] < n:
               window.pop()

           window.append(i)

           if i >= k - 1:
               answer.append(nums[window[0]])

       return answer





