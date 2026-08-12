class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        sell = 0

        for p in prices[1:]:
            if p - buy > maxProfit:
                sell = p
                maxProfit = sell - buy
            
            else:
                buy = min(p, buy)

        return maxProfit