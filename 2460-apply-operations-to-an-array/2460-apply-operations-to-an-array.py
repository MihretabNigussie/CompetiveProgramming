class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                
        # move zeros part
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
        return nums
        