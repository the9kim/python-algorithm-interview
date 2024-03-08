from typing import List


class P40_1_Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(path: List[int], index: int):
            answer.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs([], 0)

        return answer


if __name__ == '__main__':
    nums = [1, 2, 3]

    p40 = P40_1_Subsets()
    answer = p40.subsets(nums)

    print(answer)

