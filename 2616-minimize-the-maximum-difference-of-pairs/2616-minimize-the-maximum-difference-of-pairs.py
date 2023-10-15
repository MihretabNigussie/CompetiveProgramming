class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        def isValid(threshold):
            
            pointer , counter = 0 , 0
            
            while pointer < len(nums) - 1:
                
                if abs(nums[pointer] - nums[pointer + 1]) <= threshold:
                    
                    counter += 1
                    pointer += 2
                
                else:
                    pointer += 1
                
                if counter == p:
                    return True
            return False
        
        if p == 0:
            return 0
            
        
        nums.sort()
        ans = 10 ** 9
        
        left , right = -1 , (10 ** 9) + 1
        
        while left + 1 < right :
            
            mid = left + (right - left )// 2
            
            if isValid(mid):
                
                ans = mid
                right = mid
            else:
                
                left = mid
                
        return ans