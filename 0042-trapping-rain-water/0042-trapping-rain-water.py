class Solution:
    def trap(self, height: List[int]) -> int:
        
        left , right = 0, len(height)-1
        lMax = height[left]
        rMax = height[right]
        ans = 0
        
        while left < right:
            min_ = min(lMax, rMax)
            if min_ == lMax:
                left += 1
                temp = min_ - height[left]
                lMax = max(lMax ,height[left] )
            else:
                right -= 1
                temp = min_ - height[right]
                rMax = max(rMax, height[right])
            if temp > 0:
                ans += temp
        return ans
            