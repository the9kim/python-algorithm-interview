from typing import List


class P37_1_Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:

        answer = []
        pre_elements = []
        def dfs(elements: List[int]):
            if not elements:
                answer.append(list(pre_elements))

            for e in elements:
                next_elements = list(elements)
                next_elements.remove(e)
                pre_elements.append(e)
                dfs(next_elements)
                pre_elements.remove(e)

        dfs(nums)

        return answer


if __name__ == '__main__':
    nums = [1, 2, 3]
    p37 = P37_1_Permutations()
    answer = p37.permute(nums)

    print(answer)

