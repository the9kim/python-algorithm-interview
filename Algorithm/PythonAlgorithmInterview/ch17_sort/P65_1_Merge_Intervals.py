from typing import List


class P65_1_Merge_Intervals:
    def merge(self, intervals:List[List[int]])-> List[List[int]]:

        answer = []

        intervals = sorted(intervals, key=lambda x: x[0])

        for interval in intervals:
            last = None
            if answer:
                last = answer[-1]
            if answer and last[1] >= interval[0]:
                last[1] = max(last[1], interval[1])

            else:
                answer.append(interval)

        return answer

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    p65 = P65_1_Merge_Intervals()
    answer = p65.merge(intervals)


    print(answer)










