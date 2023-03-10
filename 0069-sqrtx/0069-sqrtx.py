class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = -1 , x+1
        while left + 1 < right:
            mid = left + (right- left)//2
            
            if mid ** 2 < x:
                left = mid
            elif mid ** 2 > x:
                right = mid
            else:
                return mid
        return right -1