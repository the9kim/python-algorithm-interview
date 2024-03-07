from typing import List


class P39_1_Combination_Sum:
    def combinationSum(self, candidates:List[int], target: int) -> List[List[int]]:

        answer = []
        def dfs(csum: int, path: List[int], index: int):
            if csum < 0:
                return
            elif csum == 0:
                answer.append(path.copy())
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(csum - candidates[i], path, i)
                path.pop()


        dfs(target, [], 0)

        return answer


if __name__ == '__main__':

    candidates = [2, 3, 6, 7]

    target = 7

    p39 = P39_1_Combination_Sum()

    answer = p39.combinationSum(candidates, target)

    print(answer)
