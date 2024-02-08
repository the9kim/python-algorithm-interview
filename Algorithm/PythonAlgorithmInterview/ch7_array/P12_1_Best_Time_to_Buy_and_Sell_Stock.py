class P12_1_Best_Time_to_Buy_and_Sell_Stock

    # Time exceeded
    def maxProfit(self, prices:list[int]) -> int:

        maxProfit = 0

        left = 0
        buyingPrice = float('inf')

        while left < len(prices) - 1:
            if prices[left] < buyingPrice:
                buyingPrice = prices[left]

                right = left + 1
                sellingPrice = float('-inf')
                while right < len(prices):
                    if buyingPrice < prices[right] and prices[right] > sellingPrice:
                        sellingPrice = prices[right]
                        maxProfit = max(maxProfit, sellingPrice - buyingPrice)
                    right += 1

            left += 1

        return maxProfit



    # The solution the textBook suggests
    def maxProfit2(self, prices:list[int]) -> int:

        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            # Update the minPrice
            minPrice = min(minPrice, price)

            # Update Max Profit
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

