class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        
        price = prices[0]
        
        for i in prices:
            
            if price < i:
                ans += i - price
            price = i 
        return ans
        