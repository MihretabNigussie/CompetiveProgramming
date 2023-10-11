class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        left , right = -1, (num // 2) + 1
        
        while left + 1 < right:
            
            mid = left + (right - left)//2
            
            if mid ** 2 > num:
                
                right = mid
            elif mid ** 2 < num:
                
                left = mid
            
            else:
                return True
            
        return False