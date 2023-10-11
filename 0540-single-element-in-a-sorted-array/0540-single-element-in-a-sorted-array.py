class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        left , right = -1, len(nums)
        n = len(nums)
        
        while left + 1 < right:
            
            mid = left + (right - left) // 2
            
            size = n - mid
            
            if size % 2 == 0 and nums[mid] == nums[(mid + 1) % n ] or (size % 2 == 1 and nums[(mid + 1) % n] != nums[mid]):
                right = mid
            
            else:
                left = mid
        
        return nums[right]
                                                                       
                                                                
                                                                       
                                                                       
                                                                       
            
           
        
                