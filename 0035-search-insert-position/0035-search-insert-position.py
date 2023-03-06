class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = -1 , len(nums)
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return right
        