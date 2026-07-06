class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            earn = prices[right] - prices[left]

            if earn <= 0:
                left = right
            
            profit = max(profit, earn)
            right += 1

        return profit
            