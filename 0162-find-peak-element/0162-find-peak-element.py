class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        length = len(nums) 
        if length == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1
        
        
        left, right = -1, len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left )//2
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                
                return mid
            
            elif nums[mid- 1] < nums[mid] < nums[mid + 1]:
                
                left = mid
            else:
                right = mid
        return left + 2