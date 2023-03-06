class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height)-1
        maxArea = 0
        while left < right:
            maxArea1 = min(height[left],height[right]) * (right-left)
            maxArea = max(maxArea, maxArea1)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return maxArea