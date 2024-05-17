import heapq
from typing import List
import collections

class P86_1_Task_Scheduler:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)

        heap = []
        for key, value in counter.most_common():
            heapq.heappush(heap, -(value))


        answer = 0

        while True:
            elems = []
            interval = 0

            while heap:
                elem = -heapq.heappop(heap)
                if interval < n + 1:
                    answer += 1
                    interval += 1

                    if elem > 1:
                        heapq.heappush(elems, (-(elem - 1)))

                else:
                    heapq.heappush(elems, (-elem))

            if not elems:
                break

            heap = elems
            answer += n + 1 - interval

        return answer


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2
    p86 = P86_1_Task_Scheduler()
    answer = p86.leastInterval(tasks, n)
    print(answer)
