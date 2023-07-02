class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        left , right = 0 , 1
        
        while right < len(nums):
            
            nums[left], nums[right] = nums[right] , nums[left]
            
            left += 2
            right += 2
        
        return nums
    