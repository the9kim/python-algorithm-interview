from typing import List


class P84_1_Best_Time_to_Buy_and_Sell_Stock2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i+1] - prices[i]

        return profit
