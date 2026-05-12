class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        bestProfit = 0

        for price in prices:
            bestProfit = max(bestProfit, price - minP)
            minP = min(price, minP)
        return bestProfit