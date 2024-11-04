from typing import List


def solution(users: List[List[int]], emoticons: List[int]) -> List[int]:
    rates = [10, 20, 30, 40]
    rate_combinations = []

    update_combinations(rate_combinations, rates, len(emoticons), [])

    return find_optimal_sales(users, rate_combinations, emoticons)


def update_combinations(rate_combinations: List[List[int]], rates: List[int], size: int, elems: List[int]):
    if len(elems) == size:
        rate_combinations.append(list(elems))
        return

    for rate in rates:
        elems.append(rate)
        update_combinations(rate_combinations, rates, size, elems)
        elems.pop()


def find_optimal_sales(users: List[List[int]], rate_combinations: List[List[int]], emoticons: List[int]) -> List[int]:
    sales = []

    for rates in rate_combinations:
        service_user = 0
        profit = 0

        for user in users:
            limit_rate = user[0]
            limit_amount = user[1]
            amount = 0

            for i in range(len(emoticons)):
                if rates[i] >= limit_rate:
                    amount += emoticons[i] * (1 - rates[i] * 0.01)

            if amount < limit_amount:
                profit += amount
            else:
                service_user += 1

        sales.append([service_user, profit])

    sales.sort(reverse=True)

    return sales[0]
