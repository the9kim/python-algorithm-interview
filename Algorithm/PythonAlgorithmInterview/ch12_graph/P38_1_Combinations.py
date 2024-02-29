from typing import List


class combinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        elements = []

        def dfs(index: int, length: int):
            if length == 0:
                answer.append(elements[:])
                return

            for i in range(index, n + 1):
                elements.append(i)
                dfs(i + 1, length - 1)
                elements.pop()


        dfs(1, k)

        return answer



if __name__ == '__main__':
    combinations = combinations()
    result = combinations.combine(4, 2)
    print(result)


