class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        mins= min(nums)
        maxs = max(nums)
        
        if k == 0:
            return maxs - mins
        
        if maxs - mins > 2 * k:
            
            return (maxs- k) - (mins + k)
        
        return 0