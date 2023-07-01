class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return 0 
        nums.sort()
        if len(nums) == 2:
            return nums[1] - nums[0]
        
        ans = inf
        left , right = 0, k - 1
        
        while right < len(nums):
            
            ans = min(ans ,nums[right] - nums[left])
            
            left += 1
            right += 1
        return ans
            