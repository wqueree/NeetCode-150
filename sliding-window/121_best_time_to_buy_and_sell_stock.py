from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = prices[0]
        max_profit: int = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit
