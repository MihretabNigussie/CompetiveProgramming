class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        gap = 1
        lastIdx = len(nums) - 1
        
        for i in range(lastIdx - 1, -1, -1):
            
            if nums[i] >= gap:
                gap = 1
            
            else:
                gap += 1
        if gap != 1:
            return False
        return True
                