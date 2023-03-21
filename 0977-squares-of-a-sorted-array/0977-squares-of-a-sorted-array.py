class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        lst = [0]*len(nums) 
        pointer = len(nums)-1
        left , right = 0 , len(nums)-1
        while left <= right:
            rightSqrt = nums[right] ** 2
            leftSqrt = nums[left] ** 2
            if nums[left] ** 2 < rightSqrt:
                lst[pointer] = rightSqrt
                right -= 1
            else:
                lst[pointer] = leftSqrt
                left += 1
            pointer -= 1
        return lst
                
            
                
        