from typing import List


class P3_1_Emoji_Discount_Promotion:
    '''
    1. Calculate the permutations of the input discount rates
    2. Calculate the number of service subscribers and sales revenue
    '''

    def solution(self, users: List[List[int]], emoticons: List[int]) -> List[int]:

        # 1.
        def get_permutation(permutations: List[List[int]], elems:List[int], rates: List[int]) -> None:
            if len(elems) == len(emoticons):
                permutations.append(list(elems))
                return

            for rate in rates:
                elems.append(rate)
                get_permutation(permutations, elems, rates)
                elems.pop()

        rates = [10, 20, 30, 40]
        permutations = []
        get_permutation(permutations, [], rates)


        # 2.
        answer_list = []

        for p in permutations:
            subscribers = 0
            revenue = 0

            for user in users:
                standard_rate = user[0]
                standard_amount = user[1]

                purchasing = 0

                for i, rate in enumerate(p):
                    if rate >= standard_rate:
                        purchasing += emoticons[i] * (1 - rate * 0.01)

                if purchasing >= standard_amount:
                    subscribers += 1
                else:
                    revenue += purchasing

            answer_list.append([subscribers, revenue])


        answer_list.sort(reverse=True)

        return answer_list[0]
