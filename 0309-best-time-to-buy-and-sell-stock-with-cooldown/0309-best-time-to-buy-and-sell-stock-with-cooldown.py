class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, sold_past, have_stock):

            if i == len(prices):
                return 0

            profit = dfs(i+1, False, have_stock)
            if have_stock:
                profit = max(profit, prices[i] + dfs(i+1, True, False))

            if not have_stock and not sold_past:
                profit = max(profit, -prices[i] + dfs(i + 1, True, True))

            return profit
        
        return dfs(0,False, False)