class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left , total = 0, 0
        ans = 0
        
        for right in range(len(nums)):
            
            total += nums[right]
            
            while nums[right] * (right- left + 1)> total + k:
                
                total -= nums[left]
                
                left += 1
            
            ans = max(ans, right - left + 1)
         
        return ans