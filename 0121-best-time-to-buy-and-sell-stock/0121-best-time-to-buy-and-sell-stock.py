class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        left = 0
        
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            
            ans = max(ans ,prices[right] - prices[left])
            
        return ans
            